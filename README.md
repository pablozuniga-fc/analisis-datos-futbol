# Análisis de datos de fútbol: de lo básico al estado del arte

Ruta de especialización de un ingeniero en estadística en análisis de datos de fútbol. Va desde los datos de resultados hasta el tracking, la visión por computador y el *deep learning*. Cada fase cierra con un entregable pensado para un cuerpo técnico o una dirección deportiva.

**Criterio de datos:** se trabaja siempre con los datos de mejor calidad disponibles, sean nacionales o extranjeros: StatsBomb Open Data (eventos y 360), DFL/IDSSE (tracking óptico) y football-data.co.uk (resultados y cuotas), entre otros.

## Fases

| Fase | Tema | Entregable | Estado |
|---|---|---|---|
| 0 | Fundamentos, mapa de datos y entorno | Repositorio + mapa de datos del fútbol | En curso |
| 1 | Datos de eventos y métricas descriptivas | Informe post-partido automatizado | Pendiente |
| 2 | Goles esperados (xG) | Modelo xG propio comparado con el de StatsBomb | Pendiente |
| 3 | Resultados, ratings y predicción | Pronóstico y simulación de una liga completa | Pendiente |
| 4 | Valor de las acciones (xT, VAEP, EPV) | Ranking de aporte con balón por jugador | Pendiente |
| 5 | Scouting y perfiles de jugadores | App de scouting | Pendiente |
| 6 | Táctica, estilos y balón parado | Informe de rival automatizado | Pendiente |
| 7 | Datos de tracking: espacio y control | Análisis con *pitch control* + perfil físico | Pendiente |
| 8 | Rendimiento físico y carga | Panel de carga para un plantel | Pendiente |
| 9 | Visión por computador y *deep learning* | Prototipo de video → posiciones 2D | Pendiente |
| 10 | Proyecto integrador | Caso completo de punta a punta | Pendiente |

## Estructura

```
├── environment.yml       # entorno conda «futbol» (Python 3.12)
├── environment.lock.yml  # versiones exactas instaladas
├── pyproject.toml        # instala src/futbol en modo editable
├── src/futbol/           # funciones reutilizables (rutas, carga, variables, modelos, gráficos)
├── notebooks/            # una carpeta por fase
├── apps/                 # aplicaciones Streamlit
├── reports/figures/      # figuras de los análisis
├── literatura/           # lista de lecturas (los PDF no se publican)
└── data/                 # raw / interim / processed (fuera de Git)
```

## Cómo reproducir

```powershell
conda env create -f environment.yml
conda activate futbol
pip install -e .
jupyter lab
```

Para reproducir las versiones exactas usadas, crea el entorno con `environment.lock.yml` en vez de `environment.yml`.

`socceraction` (SPADL y VAEP) va en un entorno aparte, que se crea en la fase 1: su última versión exige `numpy<2`, y PyMC, `shap` y `arviz` exigen `numpy>=2`.

## Fuentes de datos y atribución

- [StatsBomb Open Data](https://github.com/statsbomb/open-data): datos de eventos y 360 de Hudl StatsBomb, usados para aprendizaje e investigación con atribución, según sus términos.
- Las demás fuentes se citan en el notebook donde se usan.
