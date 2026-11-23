# Rein y Memmert (2016): resumen en español

**Referencia:** Rein, R. y Memmert, D. (2016). Big data and tactical analysis in elite soccer: future challenges and opportunities for sports science. *SpringerPlus*, 5, artículo 1410. DOI [10.1186/s40064-016-3108-2](https://doi.org/10.1186/s40064-016-3108-2) · PMID 27610328 · PMCID PMC4996805.

**Tipo:** artículo de revisión narrativa (no sistemática), escrito desde las ciencias del deporte, en la Universidad Alemana del Deporte de Colonia.

**Licencia:** CC BY 4.0. Este archivo es una síntesis propia en español, organizada para la ruta de especialización; no es una traducción del artículo.

---

## La tesis en un párrafo

Hasta hace poco, el análisis táctico del fútbol se apoyaba en la observación de expertos y en conteos de acciones que pierden casi todo el contexto del juego. Los sistemas de *tracking* cambiaron eso: hoy sobran datos, y el problema pasó a ser otro. Faltan métodos para procesarlos y, sobre todo, un **modelo teórico** que explique cómo se toman las decisiones tácticas e integre técnica, físico y táctica. Los autores proponen que las tecnologías de *big data* y el aprendizaje automático pueden ayudar a construir ese modelo, siempre que antes se resuelvan problemas organizacionales: quién es dueño de los datos, quién accede, cómo se protege la privacidad y quién tiene la experticia técnica.

---

## 1. Qué es la táctica

### Estrategia frente a táctica

- La **estrategia** son las decisiones previas al partido sobre cómo quiere jugar el equipo.
- La **táctica** es lo que surge durante el partido, de la interacción con el rival y de los ajustes en tiempo real.
- Los autores reconocen que la frontera es difusa: lo que ocurre en la cancha está condicionado por el plan previo. Por eso usan «táctica» para ambas cosas, el plan y sus adaptaciones.

### Táctica como gestión de espacio, tiempo y acciones

La definición práctica que adoptan es que la táctica describe cómo un equipo gestiona tres cosas:

| Dimensión | Qué significa | Ejemplo |
| --- | --- | --- |
| Espacio | Dónde ocurren las acciones y qué zonas ocupa el equipo al atacar y defender | Bloque defensivo alto o bajo |
| Tiempo | Frecuencia y duración de los eventos, y la velocidad con que se inician | Salida lenta en el tercio propio; pases a un toque en el último tercio |
| Acciones individuales | Qué tipo de acciones se ejecutan | Pérdidas, centros, pases |

### Cuatro niveles de táctica

1. **Individual:** los duelos uno contra uno, con y sin balón. Por ejemplo, si el defensor presiona al portador o se limita a cerrar líneas de pase.
2. **Grupal:** la coordinación de subgrupos, como la línea defensiva al ejecutar una trampa del fuera de juego.
3. **De equipo:** la formación (4-4-2, 4-2-3-1) y su ubicación en la cancha.
4. **De partido:** la filosofía de juego, como el contraataque o la posesión. Un estudio citado en la Bundesliga encontró que los equipos más exitosos recuperan el balón más rápido después de perderlo.

Los niveles no son independientes: lo que pasa arriba condiciona lo de abajo, y el éxito de las acciones individuales condiciona a su vez el de los niveles superiores.

### Qué influye en la táctica (figura 1 del artículo)

La táctica de un partido depende de una red de factores que interactúan:

- **Datos históricos:** rachas, resultados contra ese rival y contra otros.
- **Parámetros externos:** local o visita, tipo de competición, posición en la tabla, árbitros, clima.
- **Parámetros individuales de ambos equipos:** táctica, fisiología y técnica de cada jugador.

Además, la táctica cambia durante el partido. Por ejemplo, un cambio del rival puede obligar a reajustar la propia.

---

## 2. Por qué la táctica se estudiaba poco

- El estándar era la **observación de expertos** (entrenadores, scouts) que califican el partido según su experiencia, con manuales de codificación.
- No hay consenso sobre qué variables registrar, y estos datos tienen problemas de **objetividad y fiabilidad**.
- Como el juego es dinámico y depende del contexto, se discute hasta qué punto se pueden obtener medidas fiables.
- El análisis observacional detallado es **muy lento**, lo que limitó su uso.

### Qué cambió: la disponibilidad de datos

- Los medios difunden estadísticas de eventos detalladas de cada partido.
- Se masificaron los sistemas de *tracking*: por video, por GPS y por ondas de radio. Su calidad ya cumple estándares científicos.
- FIFA autorizó dispositivos para medir posición y fisiología en competición, y los clubes ya registran datos físicos y de *tracking* en entrenamientos.
- Aparecieron blogs de análisis con datos públicos, en el espíritu de la sabermetría del béisbol, y estudios que usan Twitter para detectar momentos clave o predecir resultados.
- Conclusión de los autores: la falta de datos dejó de ser el problema principal.

---

## 3. Cómo se ha estudiado la táctica hasta ahora

### 3.1 Fisiología y táctica

Hay muchos estudios sobre las exigencias físicas, pero pocos los conectan con la táctica:

- La distancia recorrida en cada rango de velocidad depende del nivel del rival y de la posición del jugador.
- En la Premier League, el aumento de pases a lo largo de varias temporadas se asoció con cambios tácticos.
- La formación del rival cambia lo que corre el propio equipo: más distancia contra un 4-2-3-1 que contra un 4-4-2.
- En juegos reducidos (5 contra 5), el equipo en inferioridad numérica pasa más tiempo en zonas altas de frecuencia cardíaca.

**Conclusión:** táctica y fisiología están ligadas, pero nadie sabe todavía cómo combinar ambas fuentes, ni cómo conectar la técnica individual con la táctica del equipo.

### 3.2 Análisis notacional

- Consiste en **conteos y promedios**: pases, posesión, recuperaciones, estilo de juego.
- **Limitación central:** descarta casi todo el contexto, por eso explica poco y los entrenadores lo adoptan poco.
- **Respuesta:** modelos multivariados que conservan algo de contexto. Por ejemplo, un estudio con 163 partidos de la liga noruega estimó *odds ratios* de llegar al área rival según el tipo de posesión. Contra defensas ordenadas rindieron más las posesiones largas, las iniciadas en el último tercio y las que usaron pases penetrantes. Contra defensas desordenadas también rindieron el contraataque y el pase largo.
- Otro estudio usó 19 indicadores para identificar estilos de juego, como la verticalidad de la posesión.

> **Conexión con tu formación:** un *odds ratio* sale de una regresión logística. Es el mismo GLM que usarás en la fase 2 para el xG, solo que con otra variable de respuesta.

### 3.3 El centroide del equipo

- El **centroide** es el centro geométrico de las posiciones de los jugadores de un equipo. Resume al equipo en un solo punto.
- Los centroides de ambos equipos se mueven acoplados. La distancia entre ellos cambia con el tamaño de la cancha, y los tiros al arco coinciden con más variabilidad en ese acoplamiento.
- Para medir cuán regular es ese movimiento se usó la **entropía aproximada** (ApEn), una medida de regularidad de series de tiempo. El entrenamiento táctico aumentó la regularidad en novatos, y la inferioridad numérica también la cambió.
- **Crítica de los autores:** no está claro qué representa esa «regularidad», y el centroide es una descripción muy abstracta del equipo.

### 3.4 Control del espacio

- **Área del casco convexo:** el polígono más pequeño que encierra a todos los jugadores de un equipo. El equipo que ataca cubre más área que el que defiende, y los jugadores con más experiencia cubren más área.
- **Área individual:** el rectángulo que encierra a los jugadores de campo, dividido por su número. Se achica cuando el balón está en el centro.
- **Diagramas de Voronoi:** asignan a cada jugador la zona de la cancha que está más cerca de él que de cualquier otro. Dan resultados parecidos al enfoque de área.
- **Superioridad numérica** en zonas concretas de la cancha.
- **Conclusión:** el control del espacio es central en la táctica y refleja que el juego es interactivo.

> **Conexión con la ruta:** el *pitch control* de la fase 7 es la versión probabilística del Voronoi. En vez de asignar cada punto al jugador más cercano, estima la probabilidad de que cada equipo llegue primero a ese punto, según la posición y la velocidad de los jugadores.

### 3.5 Redes de pases

- Los jugadores son **nodos** y los pases entre ellos son **aristas** con peso, según cuántos pases hubo. Así aparecen los jugadores clave, los que concentran más conexiones.
- Al agregar la posición de los pases, un estudio predijo resultados y la tabla final con un clasificador de vecinos más cercanos (*k-NN*).
- Otro estudio aplicó un modelo bayesiano latente a 241 partidos de La Liga 2013/14. Identificó patrones tácticos por equipo, cuáles eran más eficaces y cuánto aportaba cada jugador a cada patrón.

> **Conexión con la ruta:** fase 6 (redes de pases y teoría de grafos).

### 3.6 Aprendizaje automático

**Métodos con datos de posición:**
- **Detección de formaciones** con un algoritmo de esperanza-maximización (EM) sobre una temporada completa de la Premier League. Los equipos jugaban más defensivos de visita. El truco fue asignar primero un rol a cada jugador en cada momento, porque los roles cambian durante el partido.
- ***Clustering* de trayectorias** de ataque con kernels espacio-temporales. La comparación entre trayectorias no depende de qué jugador ocupa cada rol.
- **Predicción de dónde irá el balón** a partir de un campo de flujo calculado con las direcciones de carrera de los jugadores.
- **Comparación de secuencias de eventos** que terminan en gol, y *clustering* de jugadas para distinguir estilos de ataque.
- **Video:** flujo óptico, un modelo de bolsa de palabras y un *random forest* para reconocer patrones de juego. Necesitó que expertos cortaran el video a mano.

**Redes neuronales:** mapas autoorganizados de Kohonen y variantes jerárquicas para identificar formaciones automáticamente.

**Balance de los autores:**
- Casi todo estudia una sola faceta, sobre todo las formaciones.
- Falta integrar dominios: cómo interactúa la formación con la técnica individual, o qué exige físicamente cada posición táctica.
- Casi todo trabaja al nivel de equipo, no de grupo ni individual.
- La mayoría de estos estudios los hicieron grupos de ciencias de la computación, con poca participación de científicos del deporte.

### 3.7 El problema de fondo: falta un modelo teórico

- Hay muchos análisis interesantes, pero sin conexión conceptual entre ellos.
- Se ha propuesto varias veces la **teoría de sistemas dinámicos**, pero ni siquiera está definido su **espacio de fases**, es decir, qué variables describen el estado del juego.
- Una medida común es la **fase relativa**, que viene de modelar sistemas como osciladores acoplados. Sigue abierto si esa analogía sirve para el fútbol.
- Sin una descripción de mayor nivel, los análisis no llegan a los entrenadores.
- **Propuesta:** la inteligencia artificial, en particular el *deep learning*, podría ayudar a construir un modelo explicativo que integre táctica, fisiología y habilidades motoras. Necesita muchos datos de entrenamiento. Por eso destacan las redes que incorporan información previa: el conocimiento de los estudios anteriores podría restringir los modelos.

---

## 4. *Big data* y táctica

### Las tres V aplicadas al fútbol

| V | Qué es | En el fútbol |
| --- | --- | --- |
| **Volumen** | Tamaño de los datos | Un conjunto típico de datos de posición en XML pesa entre 86 y 300 MB; una temporada completa de la Bundesliga, con posición, eventos y video, ronda los 400 GB. No son petabytes, pero Excel ya no sirve: el problema es dar acceso estructurado (bases de datos, APIs). |
| **Variedad** | Heterogeneidad de formatos | Datos **estructurados** (con esquema fijo, como una base de datos relacional), **semiestructurados** (como el XML del *tracking*) y **no estructurados** (video, texto). En fútbol se mezclan posición, video, estado físico, entrenamiento, habilidad, anotaciones, historial médico y datos de blogs. |
| **Velocidad** | Ritmo al que se generan los datos | Desde flujos en tiempo real (fisiología, posición) hasta datos notacionales que llegan con retraso. |

### La arquitectura que proponen (figura 2 del artículo)

1. **Fuentes:** datos fisiológicos, de *tracking*, del cuerpo técnico, psicológicos, de scouting y del público.
2. **Almacenamiento *big data*:** guarda juntos los datos estructurados, semiestructurados y no estructurados.
3. **Sistema de aprendizaje automático:** extrae información y une las fuentes.
4. **Modelo táctico:** organizado en espacio, tiempo y acciones (las tres dimensiones de la sección 1).
5. **Visualización y reportes:** comunica los resultados en cada etapa.

Montar algo así exige mucha experticia técnica.

> **Conexión con la ruta:** tu repositorio replica esta arquitectura a escala pequeña: `data/raw` → `interim` → `processed`, DuckDB y Parquet para almacenar, modelos en `src/futbol`, y reportes y apps en Streamlit.

### Lecciones de la medicina

- La medicina personalizada enfrenta los mismos problemas: los datos están repartidos entre el Estado, empresas e instituciones de investigación, y la privacidad limita compartirlos.
- En el fútbol, los datos están en manos de **empresas, clubes e instituciones de investigación**.
- Un perfil detallado de un jugador puede afectar su carrera, y los clubes no quieren perder ventajas competitivas. Por eso la **gobernanza de los datos** debe resolverse antes de que el *big data* sea viable en la investigación.
- Los grupos de investigación pequeños no tienen experticia ni financiamiento para montar infraestructura, y la **reproducibilidad** se vuelve un problema.
- Como modelo proponen **Galaxy**, una plataforma web de genómica. Da acceso estandarizado a análisis complejos a quienes no son expertos, documenta y hace reproducible todo el procesamiento, y se puede ampliar.

---

## 5. Conclusiones de los autores

1. Llegan tiempos favorables: habrá más datos y se podrán hacer análisis más finos.
2. El *big data* puede ayudar a construir un modelo teórico más completo de la táctica.
3. Se necesita trabajo **multidisciplinario**: analistas de rendimiento, fisiólogos del ejercicio, biomecánicos y entrenadores, y sobre todo colaboración entre científicos del deporte y de la computación.
4. Las universidades deben formar a los futuros científicos del deporte para que entiendan los fundamentos teóricos y computacionales de estas técnicas, no solo para usarlas.
5. Hay que acordar cómo compartir datos y técnicas entre grupos, y mantener un intercambio estrecho con los entrenadores.
6. La propuesta también sirve para otras áreas de las ciencias del deporte.

---

## 6. Lectura crítica desde 2026

**Qué cambió desde 2016:**
- **Datos abiertos:** hoy hay eventos abiertos (StatsBomb Open Data, Wyscout público de 2019) y *tracking* abierto (DFL/IDSSE de 2025, Metrica, SkillCorner). La falta de datos para investigar se resolvió en buena parte.
- **Medir en contexto:** los modelos probabilísticos respondieron a la crítica del análisis notacional. El xG, VAEP (2019), el *pitch control* (2018) y EPV (2021) valoran cada acción según su contexto (fases 2, 4 y 7).
- **IA con conocimiento previo:** TacticAI (2024) usa redes neuronales de grafos sobre jugadas de córner y va en la línea de lo que proponían los autores (fase 9).

**Qué sigue abierto:**
- El modelo teórico integrador.
- La integración de la fisiología con la táctica (fase 8).
- La gobernanza y la privacidad de los datos de jugadores (fase 10; en Chile, Ley 21.719).

**Limitaciones del artículo:**
- Es una revisión narrativa, no sistemática: no explica cómo eligió los estudios.
- Casi no reporta tamaños de efecto.
- Propone una arquitectura sin implementarla.
- Mira el problema desde la academia, no desde las necesidades de un club.
- Lo que llama *big data* son, en rigor, gigabytes: el desafío real es de organización, no de escala.

---

## 7. Qué llevarse a la ruta

1. **Medir con contexto.** Contar acciones no basta. Esa es la motivación de las métricas por posesión (fase 1), del xG (fase 2) y del valor de las acciones (fase 4).
2. **El espacio es el eje de la táctica.** Centroide, casco convexo y Voronoi son la antesala del *pitch control* (fase 7).
3. **Las redes de pases** convierten la táctica en un grafo (fase 6).
4. **La infraestructura importa.** Datos ordenados, reproducibles y documentados son parte del trabajo, no un extra.
5. **Sin conexión con el cuerpo técnico, el análisis no sirve.** Cada entregable de la ruta está pensado para un club.

---

## 8. Glosario

| Inglés | Español | Qué es |
| --- | --- | --- |
| Notational analysis | Análisis notacional | Registro manual de acciones y conteos |
| Tracking data | Datos de seguimiento o posicionales | Posición (x, y) de jugadores y balón varias veces por segundo |
| Team centroid | Centroide del equipo | Promedio de las posiciones de los jugadores |
| Convex hull | Casco convexo | Polígono mínimo que encierra a un conjunto de puntos |
| Voronoi diagram | Diagrama de Voronoi | Partición del plano según el punto más cercano |
| Approximate entropy (ApEn) | Entropía aproximada | Medida de regularidad de una serie de tiempo |
| Relative phase | Fase relativa | Sincronía entre dos osciladores; aquí, entre jugadores o equipos |
| Phase space | Espacio de fases | Conjunto de variables que describen el estado de un sistema dinámico |
| Passing network | Red de pases | Grafo de jugadores (nodos) y pases (aristas) |
| Small-sided games | Juegos reducidos | Partidos de entrenamiento con menos jugadores (por ejemplo, 5 contra 5) |
| Score-box possession | Posesión que llega al área | Posesión que termina dentro del área rival |
| Expectation-maximization (EM) | Esperanza-maximización | Algoritmo para estimar modelos con variables latentes |
| Self-organizing map (Kohonen) | Mapa autoorganizado | Red neuronal no supervisada que agrupa patrones |
| Optical flow | Flujo óptico | Movimiento aparente de los píxeles entre cuadros de video |
| Data governance | Gobernanza de datos | Reglas sobre propiedad, acceso, uso y privacidad de los datos |
| Quantified self | Autocuantificación | Registro personal de datos fisiológicos y de actividad |

---

## Pistas para las preguntas guía (pestaña «Fase 0 · Teoría» del doc)

1. **Qué entienden por *big data*:** sección 4 de este resumen (las tres V y las fuentes).
2. **Por qué no basta con contar acciones:** sección 3.2 (análisis notacional) y sección 2.
3. **Qué proponen para el análisis táctico con datos de posición:** secciones 3.3 a 3.7.
4. **Qué separa a la investigación de los clubes:** secciones 3.6 (balance), 3.7 y 5.

Responde con tus propias palabras en el doc; así es como se fija lo leído.
