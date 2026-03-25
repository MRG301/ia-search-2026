# search.py
# ---------
# Algoritmos genéricos de búsqueda (sin typing):
# DFS, BFS, UCS, A*

import util


class SearchProblem:
    """
    Interfaz mínima que debe implementar un problema de búsqueda.
    """
    def getStartState(self):
        raise NotImplementedError

    def isGoalState(self, state):
        raise NotImplementedError

    def getSuccessors(self, state):
        """
        Debe regresar lista de triples:
          (successor_state, action, stepCost)
        """
        raise NotImplementedError

    def getCostOfActions(self, actions):
        raise NotImplementedError


#############################################DFS

def depthFirstSearch(problem):
    """
    DFS Grafo: Usa Stack y un conjunto de visitados.
    """
    n_generados = 0
    n_expandidos = 0
    
    frontera = util.Stack()
    visitados = set()

    inicio = problem.getStartState()
    frontera.push((inicio, []))
    n_generados += 1

    while not frontera.isEmpty():
        estado, camino = frontera.pop()

        if estado in visitados:
            continue
            
        n_expandidos += 1
        if problem.isGoalState(estado):
            return camino, n_generados, n_expandidos
            
        visitados.add(estado)

        for sucesor, accion, costo in problem.getSuccessors(estado):
            if sucesor not in visitados:
                frontera.push((sucesor, camino + [accion]))
                n_generados += 1

    return [], n_generados, n_expandidos


def dfs_tree(problem):
    """
    DFS Árbol: Sin conjunto de visitados. 
    ¡Cuidado! En el problema de las jarras puede no terminar nunca.
    """
    n_generados = 0
    n_expandidos = 0
    
    frontera = util.Stack()
    inicio = problem.getStartState()
    
    frontera.push((inicio, []))
    n_generados += 1

    # Límite de seguridad opcional para evitar que el script se cuelgue
    MAX_EXPANSIONES = 10000 

    while not frontera.isEmpty():
        estado, camino = frontera.pop()
        n_expandidos += 1

        if problem.isGoalState(estado):
            return camino, n_generados, n_expandidos
            
        if n_expandidos > MAX_EXPANSIONES:
            print("DFS Árbol abortado: Posible bucle infinito o grafo muy grande.")
            return [], n_generados, n_expandidos

        for sucesor, accion, costo in problem.getSuccessors(estado):
            frontera.push((sucesor, camino + [accion]))
            n_generados += 1

    return [], n_generados, n_expandidos

#######################################################


# search.py (Fragmento modificado)

def breadthFirstSearch(problem):
    """BFS Grafo"""
    n_generados, n_expandidos = 0, 0
    frontera = util.Queue()
    visitados = set()
    
    inicio = problem.getStartState()
    frontera.push((inicio, []))
    n_generados += 1
    visitados.add(inicio)

    while not frontera.isEmpty():
        estado, camino = frontera.pop()
        n_expandidos += 1
        if problem.isGoalState(estado): return camino, n_generados, n_expandidos

        for sucesor, accion, costo in problem.getSuccessors(estado):
            if sucesor not in visitados:
                visitados.add(sucesor)
                frontera.push((sucesor, camino + [accion]))
                n_generados += 1
    return [], n_generados, n_expandidos


def bfs_tree(problem):
    """BFS Árbol (Sin set de visitados)"""
    n_generados, n_expandidos = 0, 0
    frontera = util.Queue()
    inicio = problem.getStartState()
    frontera.push((inicio, []))
    n_generados += 1

    while not frontera.isEmpty():
        estado, camino = frontera.pop()
        n_expandidos += 1
        if problem.isGoalState(estado): return camino, n_generados, n_expandidos

        for sucesor, accion, costo in problem.getSuccessors(estado):
            frontera.push((sucesor, camino + [accion]))
            n_generados += 1
    return [], n_generados, n_expandidos

#####################################################################3

def uniformCostSearch(problem):
    
    # algoritmo UCS, usa PriorityQueue por costo acumulado g(n), sin costos no negativos.

    n_generados = 0
    n_expandidos = 0
    
    frontera = util.PriorityQueue()
    best_g = {}  # estado con el mejor costo encontrado

    inicio = problem.getStartState()
    # frontera = (estado, camino, costo_acumulado) y la prioridad
    frontera.push((inicio, [], 0), 0)
    n_generados += 1
    best_g[inicio] = 0

    while not frontera.isEmpty():
        estado, camino, g = frontera.pop()

        # Si encontramos una ruta con menor costo hacia este estado antes de sacarlo, lo ignoramos
        if g > best_g.get(estado, float("inf")):
            continue
            
        n_expandidos += 1

        if problem.isGoalState(estado):
            return camino, n_generados, n_expandidos

        for sucesor, accion, step_cost in problem.getSuccessors(estado):
            nuevo_g = g + step_cost
            if nuevo_g < best_g.get(sucesor, float("inf")):
                best_g[sucesor] = nuevo_g
                frontera.push((sucesor, camino + [accion], nuevo_g), nuevo_g)
                n_generados += 1

    return [], n_generados, n_expandidos

def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    A*: usa PriorityQueue con f(n) = g(n) + h(n).
    Optimalidad si h es admisible (y consistente).
    """
    frontera = util.PriorityQueue()
    best_g = {}

    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return []

    g0 = 0
    f0 = g0 + heuristic(inicio, problem)
    frontera.push((inicio, [], g0), f0)
    best_g[inicio] = g0

    while not frontera.isEmpty():
        estado, camino, g = frontera.pop()

        if g > best_g.get(estado, float("inf")):
            continue

        if problem.isGoalState(estado):
            return camino

        for sucesor, accion, step_cost in problem.getSuccessors(estado):
            nuevo_g = g + step_cost
            if nuevo_g < best_g.get(sucesor, float("inf")):
                best_g[sucesor] = nuevo_g
                nuevo_f = nuevo_g + heuristic(sucesor, problem)
                frontera.push((sucesor, camino + [accion], nuevo_g), nuevo_f)

    return []

def bestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Primero el Mejor o Best First Search: tambien usa PriorityQueue, pero con f(n) = h(n)
    La busqueda se guia, con que tan cerca parece estar de la meta
    """
    frontera = util.PriorityQueue()
    visitados = set()

    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return []

    # En primero el mejor, f(n) es puramente la heuristica h(n), sin el costo acumulado
    f0 = heuristic(inicio, problem)
    # en la tupla se quito 'g' ya que no es necesario
    frontera.push((inicio, []), f0)

    while not frontera.isEmpty():
        estado, camino = frontera.pop()

        # se modifico el control de visitados mas simple
        if estado in visitados:
            continue
        visitados.add(estado)

        if problem.isGoalState(estado):
            return camino

        for sucesor, accion, step_cost in problem.getSuccessors(estado):
            if sucesor not in visitados:
                # la heuristica del sucesor, sin nuevo_g
                nuevo_f = heuristic(sucesor, problem)
                frontera.push((sucesor, camino + [accion]), nuevo_f)

    return []

########################################################IDDFS

def depthLimitedSearch(problem, limit):
    """
    DFS con límite de profundidad y conteo de nodos.
    """
    n_generados = 0
    n_expandidos = 0
    
    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return [], 0, 0
    
    # Elemento: (estado, camino, profundidad, ruta_actual)
    # ruta_actual es un set para búsqueda O(1) de ciclos en la rama
    frontera = util.Stack()
    frontera.push((inicio, [], 0, {inicio}))
    n_generados += 1

    while not frontera.isEmpty():
        estado, camino, profundidad, ruta_actual = frontera.pop()
        n_expandidos += 1

        if problem.isGoalState(estado):
            return camino, n_generados, n_expandidos

        # Solo expandimos si no hemos alcanzado el límite
        if profundidad < limit:
            for sucesor, accion, costo in problem.getSuccessors(estado):
                if sucesor not in ruta_actual:
                    nueva_ruta = ruta_actual.copy()
                    nueva_ruta.add(sucesor)
                    frontera.push((sucesor, camino + [accion], profundidad + 1, nueva_ruta))
                    n_generados += 1
                    
    return None, n_generados, n_expandidos





def iterativeDeepeningSearch(problem, max_depth=50):
    """
    Búsqueda en profundidad iterativa (IDDFS).
    """
    total_generados = 0
    total_expandidos = 0

    for limite in range(max_depth + 1):
        # Ejecutamos DLS para el límite actual
        resultado, gen, exp = depthLimitedSearch(problem, limite)
        
        total_generados += gen
        total_expandidos += exp
        
        # Si resultado no es None, encontramos la meta
        if resultado is not None:
            return resultado, total_generados, total_expandidos
            
    return [], total_generados, total_expandidos




# Alias
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch