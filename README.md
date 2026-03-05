# IA Search 2026

Repositorio de prácticas para la asignatura **Inteligencia Artificial**.

En este proyecto se implementan y analizan distintos **algoritmos de
búsqueda en espacios de estados**, tales como:

-   Breadth First Search (BFS)
-   Depth First Search (DFS)
-   Uniform Cost Search (UCS)

El objetivo de la práctica es que los estudiantes comprendan cómo
modelar problemas como **problemas de búsqueda** y cómo aplicar
distintos algoritmos para resolverlos.

------------------------------------------------------------------------

## Estructura del proyecto

    ia-search-2026
    │
    ├── problems/                # Definición de problemas de búsqueda
    │   └── jarras.py
    │
    ├── visualizacion/           # Visualización de la ejecución de algoritmos
    │   └── animacion_bfs_jarras.py
    │
    ├── search.py                # Implementación de algoritmos de búsqueda
    ├── util.py                  # Estructuras de datos auxiliares
    ├── requirements.txt         # Dependencias del proyecto
    └── README.md

------------------------------------------------------------------------

## Requisitos

Se requiere:

-   Python 3.10 o superior
-   pip

------------------------------------------------------------------------

## Instalación

Clonar el repositorio:

``` bash
git clone https://github.com/lirc2911/ia-search-2026.git
cd ia-search-2026
```

Crear entorno virtual:

``` bash
python -m venv venv
```

Activar entorno virtual

**Windows**

``` bash
venv\Scripts\activate
```

**Mac / Linux**

``` bash
source venv/bin/activate
```

Instalar dependencias

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Ejecución

Ejemplo de ejecución del problema de las jarras:

``` bash
python visualizacion/main.py
```

Esto mostrará los resultados de la ejecución de cada uno de los algoritmos. 

------------------------------------------------------------------------


## Objetivos de aprendizaje

Al finalizar la práctica el estudiante deberá ser capaz de:

-   Modelar problemas como **espacios de estados**
-   Definir **función sucesora**
-   Implementar algoritmos de búsqueda
-   Analizar el comportamiento de distintos algoritmos

------------------------------------------------------------------------

## Autores

Curso: **Inteligencia Artificial**\
Universidad Autónoma de la Ciudad de México (UACM)\
2026
