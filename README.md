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
    |   └── canivales.py         # Version de canivales con cientificos y muestras
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

## Modelado del Problema: Científicos y Muestras Biológicas

Este proyecto incluye la implementación de un problema de 
búsqueda basado en el clásico "Misioneros y Caníbales", 
adaptado a un contexto de científicos y muestras biologicas
inestables.

## Representación del Estado

Para que los algoritmos de búsqueda puedan procesar el entorno,
el estado se definió como una estructura inmutable utilizando 
una tupla de tres elementos: (cientificos_izq, muestras_izq, bote_izq).

-   cientificos_izq: Número que representa la cantidad de científicos
 en la orilla A.

-   muestras_izq: Número que representa la cantidad de muestras en la 
orilla A.

-   bote_izq: Valor binario donde 1 indica que la balsa está en la Orilla 
A y 0 indica que está en la Orilla B.

El estado inicial se define como (3, 3, 1) y el estado meta como (0, 0, 0).

## Restricciones Implementadas

El modelo valida cada transición para evitar estados irreales o 
que violen las reglas del problema

-   Los límites físicos, no se permiten valores negativos ni cantidades 
que superen el total de individuos que son 3 científicos y 3 muestras.


-   Ls capacidad de transporte, la balsa puede mover a un máximo de 2 
entidades y un mínimo de 1 por viaje.


-   La regla de contaminación, si en una orilla hay al menos un 
científico, la cantidad de muestras no puede ser estrictamente
 mayor que la de científicos, si esto ocurre, las muestras se 
 vuelven inestables y el estado se descarta como inválido.

## Justificación del Diseño

-   se eligió una tupla de 3 variables en lugar de 5
 porque las tuplas son objetos inmutables en Python, esto es 
un requisito para poder almacenar los estados generados en el 
conjunto de nodos visitados y evitar ciclos infinitos.
-   con esto optimizamos la memoria, ya que solo se rastrea la información
de la orilla izquierda, los valores de la orilla derecha se 
calculan dinámicamente mediante una simple resta, por ejemplo,
 cientificos_der = 3 - cientificos_izq, esto reduce la redundancia
 de datos y minimiza el uso de memoria durante la expansión de la frontera.

## Reflexión Comparativa

A diferencia del problema de las Jarras, que cuenta con un espacio de
estados máximo de 20, limitado por las capacidades discretas de 5x4,
el problema de los científicos posee un espacio teórico de 32 estados
4 * 4 * 2, al ejecutar los algoritmos, se observaron las siguientes diferencias:
-   BFS y UCS, ambos algoritmos resultaron ser los más eficientes
y confiables para este problema, al tener un costo de acción 
uniforme de 1 por viaje, garantizan encontrar la solución óptima,
la cual consta de 11 pasos generados y 15 nodos expandidos.
-   DFS, aunque la búsqueda en profundidad versión grafo logra
encontrar la solución en 11 pasos, su rendimiento es diferente, 
expandiendo 12 nodos y generando 16, sin embargo, DFS demostró 
ser muy susceptible al factor de ramificación y a las transiciones
altamente cíclicas, es decir, la balsa yendo y viniendo, sin un estricto 
control de memoria de estados visitados, DFS corre el riesgo de 
caer en ramas ineficientes o bucles infinitos.