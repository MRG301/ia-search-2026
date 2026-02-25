# problems/jarras.py
# ------------------
# Problema clásico de las jarras de agua (Water Jug Problem).
#
# Estado: (a, b)
#   a = cantidad de agua en jarra A
#   b = cantidad de agua en jarra B
#
# Acciones típicas:
# - Llenar A / Llenar B
# - Vaciar A / Vaciar B
# - Verter A -> B
# - Verter B -> A
#
# Costo: 1 por acción (puedes cambiarlo si quieres)

class JarrasProblem:
    def __init__(self, capA=4, capB=3, start=(0, 0), goal=(2, 0)):
        self.capA = capA
        self.capB = capB
        self.start = start
        self.goal = goal

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        a, b = state
        sucesores = []

        # 1) Llenar A
        if a < self.capA:
            sucesores.append(((self.capA, b), "Llenar A", 1))

        # 2) Llenar B
        if b < self.capB:
            sucesores.append(((a, self.capB), "Llenar B", 1))

        # 3) Vaciar A
        if a > 0:
            sucesores.append(((0, b), "Vaciar A", 1))

        # 4) Vaciar B
        if b > 0:
            sucesores.append(((a, 0), "Vaciar B", 1))

        # 5) Verter A -> B (pasar agua de A a B hasta llenar B o vaciar A)
        if a > 0 and b < self.capB:
            espacio_en_B = self.capB - b
            cantidad = min(a, espacio_en_B)
            nuevo = (a - cantidad, b + cantidad)
            sucesores.append((nuevo, "Verter A->B", 1))

        # 6) Verter B -> A
        if b > 0 and a < self.capA:
            espacio_en_A = self.capA - a
            cantidad = min(b, espacio_en_A)
            nuevo = (a + cantidad, b - cantidad)
            sucesores.append((nuevo, "Verter B->A", 1))

        return sucesores

    def getCostOfActions(self, actions):
        # Cada acción cuesta 1
        return len(actions)