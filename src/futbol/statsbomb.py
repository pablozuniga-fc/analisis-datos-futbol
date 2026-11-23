"""Descarga y caché local de StatsBomb Open Data.

Cada partido se descarga una sola vez y se guarda en Parquet en
data/raw/statsbomb/<competition_id>_<season_id>/ (fuera de Git). Las lecturas
siguientes son locales y se hacen con DuckDB, que une archivos con columnas
distintas (no todos los partidos tienen los mismos tipos de evento).
"""

from __future__ import annotations

import json
import math
import warnings
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import duckdb
import pandas as pd
from statsbombpy import sb

from futbol.rutas import CRUDOS

warnings.filterwarnings("ignore", message="credentials were not supplied")

CARPETA = CRUDOS / "statsbomb"


def buscar_ids(competicion: str, temporada: str) -> tuple[int, int]:
    """Devuelve (competition_id, season_id) a partir de los nombres de StatsBomb."""
    comps = sb.competitions()
    fila = comps[(comps["competition_name"] == competicion) & (comps["season_name"] == temporada)]
    if fila.empty:
        raise ValueError(f"No existe «{competicion} {temporada}» en StatsBomb Open Data")
    return int(fila["competition_id"].iloc[0]), int(fila["season_id"].iloc[0])


def _carpeta(competition_id: int, season_id: int) -> Path:
    return CARPETA / f"{competition_id}_{season_id}"


def _vacio(valor) -> bool:
    return valor is None or (isinstance(valor, float) and math.isnan(valor))


def _es_anidado(valor) -> bool:
    if isinstance(valor, dict):
        return True
    return isinstance(valor, list) and any(isinstance(x, (dict, list)) for x in valor)


def _a_parquet(df: pd.DataFrame, ruta: Path) -> None:
    """Guarda en Parquet. Parquet exige un solo tipo por columna, así que:

    - las columnas con diccionarios o listas anidadas pasan a texto JSON;
    - las columnas que mezclan tipos (por ejemplo, un id numérico y «4711, 3626»
      cuando hay dos entrenadores) pasan a texto.
    """
    df = df.copy()
    for col in df.columns:
        if df[col].dtype != object:
            continue
        valores = df[col].dropna()
        if valores.map(_es_anidado).any():
            df[col] = df[col].map(
                lambda v: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else (None if _vacio(v) else v)
            )
        elif valores.map(type).nunique() > 1:
            df[col] = df[col].map(lambda v: None if _vacio(v) else str(v))
    ruta.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta, index=False)


def partidos(competition_id: int, season_id: int) -> pd.DataFrame:
    """Partidos de una competición y temporada (con caché local)."""
    ruta = _carpeta(competition_id, season_id) / "partidos.parquet"
    if not ruta.exists():
        _a_parquet(sb.matches(competition_id=competition_id, season_id=season_id), ruta)
    return pd.read_parquet(ruta)


def _descargar_eventos(match_id: int, carpeta: Path) -> None:
    ruta = carpeta / "eventos" / f"{match_id}.parquet"
    if not ruta.exists():
        _a_parquet(sb.events(match_id=match_id), ruta)


def descargar_temporada(competition_id: int, season_id: int, hilos: int = 4) -> int:
    """Descarga los eventos de todos los partidos que falten. Devuelve cuántos partidos hay en caché."""
    carpeta = _carpeta(competition_id, season_id)
    ids = partidos(competition_id, season_id)["match_id"].astype(int).tolist()
    with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
        list(ejecutor.map(lambda m: _descargar_eventos(m, carpeta), ids))
    return len(list((carpeta / "eventos").glob("*.parquet")))


def eventos(competition_id: int, season_id: int, columnas: list[str] | None = None) -> pd.DataFrame:
    """Eventos de toda la temporada desde la caché local (descarga lo que falte).

    `columnas` limita lo que se carga en memoria; sin ella se cargan todas (más de 100).
    """
    descargar_temporada(competition_id, season_id)
    patron = (_carpeta(competition_id, season_id) / "eventos" / "*.parquet").as_posix()
    seleccion = "*" if columnas is None else ", ".join(f'"{c}"' for c in columnas)
    consulta = f"SELECT {seleccion} FROM read_parquet('{patron}', union_by_name = true)"
    with duckdb.connect() as con:
        con.execute("SET enable_progress_bar = false")
        return con.execute(consulta).df()
