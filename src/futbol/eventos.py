"""Funciones sobre datos de eventos de StatsBomb."""

from __future__ import annotations

import json

import pandas as pd

# Columnas que necesita minutos_jugados()
COLUMNAS_MINUTOS = [
    "match_id",
    "team",
    "type",
    "minute",
    "second",
    "player",
    "player_id",
    "tactics",
    "substitution_replacement",
    "substitution_replacement_id",
    "foul_committed_card",
    "bad_behaviour_card",
]

TARJETAS_ROJAS = {"Red Card", "Second Yellow"}


def tiempo(eventos: pd.DataFrame) -> pd.Series:
    """Minuto del partido en decimales. StatsBomb acumula: el segundo tiempo empieza en 45."""
    return eventos["minute"] + eventos["second"] / 60


def minutos_jugados(eventos: pd.DataFrame) -> pd.DataFrame:
    """Minutos jugados por jugador y partido, calculados desde los eventos.

    - Los titulares (evento «Starting XI») entran en el minuto 0.
    - Los suplentes entran en el minuto de su cambio («Substitution»).
    - Un jugador sale por cambio, por expulsión (roja directa o segunda amarilla)
      o al final del partido, que es el último evento registrado.
    """
    ev = eventos.assign(t=tiempo(eventos))
    fin_partido = ev.groupby("match_id")["t"].max().rename("fin_partido")

    titulares = []
    for fila in ev.loc[ev["type"] == "Starting XI", ["match_id", "team", "tactics"]].itertuples(index=False):
        tacticas = json.loads(fila.tactics) if isinstance(fila.tactics, str) else fila.tactics
        for jugador in tacticas["lineup"]:
            titulares.append(
                {
                    "match_id": fila.match_id,
                    "team": fila.team,
                    "player_id": jugador["player"]["id"],
                    "player": jugador["player"]["name"],
                    "entrada": 0.0,
                }
            )

    cambios = ev[ev["type"] == "Substitution"]
    suplentes = pd.DataFrame(
        {
            "match_id": cambios["match_id"],
            "team": cambios["team"],
            "player_id": cambios["substitution_replacement_id"],
            "player": cambios["substitution_replacement"],
            "entrada": cambios["t"],
        }
    )
    jugadores = pd.concat([pd.DataFrame(titulares), suplentes], ignore_index=True)
    jugadores["player_id"] = jugadores["player_id"].astype(int)

    expulsion = ev["foul_committed_card"].isin(TARJETAS_ROJAS) | ev["bad_behaviour_card"].isin(TARJETAS_ROJAS)
    salidas = pd.concat([cambios[["match_id", "player_id", "t"]], ev.loc[expulsion, ["match_id", "player_id", "t"]]])
    salidas = salidas.dropna().astype({"player_id": int})
    salidas = salidas.groupby(["match_id", "player_id"])["t"].min().rename("salida")

    resultado = jugadores.join(salidas, on=["match_id", "player_id"]).join(fin_partido, on="match_id")
    resultado["salida"] = resultado["salida"].fillna(resultado["fin_partido"])
    resultado["minutos"] = (resultado["salida"] - resultado["entrada"]).clip(lower=0)
    return resultado[["match_id", "team", "player_id", "player", "entrada", "salida", "minutos"]]


def por_90(cantidad: pd.Series, minutos: pd.Series) -> pd.Series:
    """Tasa por 90 minutos: 90 × cantidad / minutos."""
    return 90 * cantidad / minutos
