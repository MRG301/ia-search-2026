# main.py
# ------
# Prueba simple de DFS/BFS/UCS/A* con un grafo pequeño.

# Ejecuta DFS/BFSUCS/A* sobre el problema de las jarras.

from search import dfs, bfs, ucs, astar, nullHeuristic
from problems.jarras import JarrasProblem
from problems.canibales import CanibalesLikeProblem

# Definición de un problema de grafo simple para probar los algoritmos de búsqueda.
'''class ProblemaGrafo:
    
      A -> B (1), A -> C (2)
      B -> D (5)
      C -> D (1)
    Inicio: A
    Meta: D
    """
    def __init__(self):
        self.inicio = "A"
        self.meta = "D"
        self.grafo = {
            "A": [("B", "A->B", 1), ("C", "A->C", 2)],
            "B": [("D", "B->D", 5)],
            "C": [("D", "C->D", 1)],
            "D": []
        }
        self.costos_accion = {
            "A->B": 1,
            "A->C": 2,
            "B->D": 5,
            "C->D": 1
        }

    def getStartState(self):
        return self.inicio

    def isGoalState(self, state):
        return state == self.meta

    def getSuccessors(self, state):
        return self.grafo[state]

    def getCostOfActions(self, actions):
        total = 0
        for a in actions:
            total += self.costos_accion[a]
        return total

'''
# Probamos los algoritmos de búsqueda sobre el grafo definido.
#def main():
#    problema = ProblemaGrafo()

#    sol_dfs = dfs(problema)
#    sol_bfs = bfs(problema)
#    sol_ucs = ucs(problema)
#    sol_astar = astar(problema, heuristic=nullHeuristic)

#    print("DFS :", sol_dfs, " costo:", problema.getCostOfActions(sol_dfs) if sol_dfs else 0)
#    print("BFS :", sol_bfs, " costo:", problema.getCostOfActions(sol_bfs) if sol_bfs else 0)
#    print("UCS :", sol_ucs, " costo:", problema.getCostOfActions(sol_ucs) if sol_ucs else 0)
#    print("A*  :", sol_astar, " costo:", problema.getCostOfActions(sol_astar) if sol_astar else 0)

'''
# Probamos con el problema de las jarras. 
def main():
    # Ejemplo clásico: jarra A de 5L, jarra B de 3L, meta (2,0)
    problema = JarrasProblem(capA=5, capB=3, start=(0, 0), goal=(2, 0))

    sol_bfs = bfs(problema)
    sol_ucs = ucs(problema)
    sol_astar = astar(problema, heuristic=nullHeuristic)  # con h=0, A* = UCS

    print("========================================")
    print(" Problema de las Jarras")
    print(" Capacidad A =", problema.capA, " Capacidad B =", problema.capB)
    print(" Inicio =", problema.start, " Meta =", problema.goal)
    print("========================================\n")

    print("BFS (menos pasos):")
    print(sol_bfs)
    print("Costo:", problema.getCostOfActions(sol_bfs))
    print()

    print("UCS (menor costo):")
    print(sol_ucs)
    print("Costo:", problema.getCostOfActions(sol_ucs))
    print()

    # Si quieres ver DFS también (ojo: puede dar rutas largas dependiendo del orden de sucesores)
    sol_dfs = dfs(problema)
    print("DFS (puede no ser óptimo):")
    print(sol_dfs)
    print("Costo:", problema.getCostOfActions(sol_dfs))
'''
'''
# En main.py
def ejecutar_experimento(nombre, funcion, problema):
    camino, gen, exp = funcion(problema)
    termina = "Sí" if camino or exp > 0 else "No"
    longitud = len(camino)
    print(f"{nombre:10} | {gen:10} | {exp:10} | {termina:8} | {longitud:8}")

def main():
    from search import bfs, bfs_tree, dfs, dfs_tree,iterativeDeepeningSearch # Asegúrate de importarlas
    
    # Usando el problema de las jarras definido en tu archivo
    problema = JarrasProblem(capA=5, capB=3, start=(0, 0), goal=(2, 0))

    print(f"{'Algoritmo':10} | {'Generados':10} | {'Expandidos':10} | {'Termina':8} | {'Longitud':8}")
    print("-" * 60)
    
    ejecutar_experimento("BFS Grafo", bfs, problema)
    ejecutar_experimento("BFS Árbol", bfs_tree, problema)
    ejecutar_experimento("DFS Grafo", dfs, problema)
    ejecutar_experimento("DFS Árbol", dfs_tree, problema) 
    ejecutar_experimento("IDDFS", iterativeDeepeningSearch, problema)
    # Cuidado: DFS Árbol puede entrar en bucle infinito si hay ciclos
    # ejecutar_experimento("DFS Árbol", dfs_tree, problema)    
'''




'''
# Probamos los algoritmos de búsqueda sobre el grafo definido.
def main():
    problema = ProblemaGrafo()

    sol_dfs = dfs(problema)
    sol_bfs = bfs(problema)
    sol_ucs = ucs(problema)
    sol_astar = astar(problema, heuristic=nullHeuristic)

    #Para el experimento sobre busqueda de arbol y grafo con ciclo
    sol_dfst = dfst(problema)
    sol_bfst = bfst(problema)

    print("DFS grafo :", sol_dfs, " costo:", problema.getCostOfActions(sol_dfs) if sol_dfs else 0)
    print("BFS grafo :", sol_bfs, " costo:", problema.getCostOfActions(sol_bfs) if sol_bfs else 0)
    print("DFS arbol :", sol_dfst, " costo:", problema.getCostOfActions(sol_dfst) if sol_dfst else 0)
    print("BFS arbol :", sol_bfst, " costo:", problema.getCostOfActions(sol_bfst) if sol_bfst else 0)
    print("UCS :", sol_ucs, " costo:", problema.getCostOfActions(sol_ucs) if sol_ucs else 0)
    print("A*  :", sol_astar, " costo:", problema.getCostOfActions(sol_astar) if sol_astar else 0)


################################################	search.py	###################################################


#Busqueda de primero en profundidad (arbol)
def depthFirstSearchTree(problem):
    #DFS en árbol (sin visitados) con límite de nodos
    frontera = util.Stack()
    inicio = problem.getStartState()
    frontera.push((inicio, [])) # (estado, camino)
    
    #Solo se coloca para que no muera la PC
    contador = 0
    limite=1000

    while not frontera.isEmpty():
        estado, camino = frontera.pop()
        contador += 1

        if contador > limite:
            print("Busqueda de primero en profundidad: el arbol se ciclo de manera infinita no es posible colocar el camino obtenido")
            return []

        if problem.isGoalState(estado):
            return camino

        #Se invierte el orden de sucesores para conservar el orden de llegada a la pila 
        #se guarda primero G y luego A para que la generación del arbol sea la adecuada
        for sucesor, accion, costo in reversed(problem.getSuccessors(estado)):  
            frontera.push((sucesor, camino + [accion]))

    return []

#Busqueda de primero en amplitud (arbol)
def breadthFirstSearchTree(problem):
    #BFS: en árbol (sin visitados) con límite de nodos
    frontera = util.Queue()
    inicio = problem.getStartState()
    frontera.push((inicio, []))
    
    #Solo se colocan para que no muera la PC
    contador = 0
    limite=1000 

    while not frontera.isEmpty():
        estado, camino = frontera.pop()
        contador += 1

        if contador > limite:
            print("Busqueda de primero en amplitud: el arbol se ciclo de manera infinita no es posible colocar el camino obtenido")
            return []
        
        if problem.isGoalState(estado):
            return camino

        for sucesor, accion, costo in problem.getSuccessors(estado):
            frontera.push((sucesor, camino + [accion]))

    return []




########################### hasta abajo del search.py ###########################
#alias extras
dfst = depthFirstSearchTree
bfst = breadthFirstSearchTree
'''



 

def ejecutar_experimento(nombre, funcion, problema):
    camino, gen, exp = funcion(problema)
    termina = "Sí" if camino or exp > 0 else "No"
    longitud = len(camino) if camino else 0
    costo = problema.getCostOfActions(camino) if camino else 0
    
    print(f"{nombre:20} | {gen:10} | {exp:10} | {termina:8} | {longitud:8} | {costo:6}")

def main():
    prob_jarras = JarrasProblem(capA=5, capB=3, start=(0, 0), goal=(2, 0))
    
    prob_cientificos = CanibalesLikeProblem()

    print(f"{'Algoritmo y Problema':20} | {'Generados':10} | {'Expandidos':10} | {'Termina':8} | {'Longitud':8} | {'Costo':6}")
    print("-" * 75)
    
    ejecutar_experimento("Jarras BFS", bfs, prob_jarras)
    ejecutar_experimento("Jarras DFS", dfs, prob_jarras)
    ejecutar_experimento("Jarras UCS", ucs, prob_jarras)
    print("-" * 75)
    ejecutar_experimento("Cientificos BFS", bfs, prob_cientificos)
    ejecutar_experimento("Cientificos DFS", dfs, prob_cientificos)
    ejecutar_experimento("Cientificos UCS", ucs, prob_cientificos)

if __name__ == "__main__":
    main()
