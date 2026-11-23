"""Rutas del proyecto, calculadas desde la raíz del repositorio."""

from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

DATOS = RAIZ / "data"
CRUDOS = DATOS / "raw"
INTERMEDIOS = DATOS / "interim"
PROCESADOS = DATOS / "processed"
FIGURAS = RAIZ / "reports" / "figures"

# Datos pesados (tracking, video) fuera de OneDrive para no saturar la sincronización.
# Se usa desde la fase 7.
CACHE_PESADA = Path.home() / "futbol-data"


def asegurar_carpetas() -> None:
    """Crea las carpetas de datos y figuras si no existen."""
    for carpeta in (CRUDOS, INTERMEDIOS, PROCESADOS, FIGURAS):
        carpeta.mkdir(parents=True, exist_ok=True)
