# problems/canibales_like.py
# -------------------------
# PRÁCTICA (Parte 2): Modelar un problema de búsqueda tipo "misioneros y caníbales"
#
# Propósito:
# - Definir estados
# - Definir acciones y transiciones (getSuccessors)
# - Definir restricciones (estados inválidos)
# - Definir meta
#
# Problema base sugerido (misioneros y caníbales clásico):
# - Hay M misioneros y C caníbales en la orilla izquierda.
# - Un bote puede transportar 1 o 2 personas.
# - Restricción: en cualquier orilla, si hay misioneros > 0,
#   entonces misioneros >= caníbales (para que no "se los coman").
#
# Puedes usar el clásico o adaptar el tema (robots/virus, admins/hackers, etc.)
# siempre que sea isomorfo: mismos tipos de restricciones.

from search import SearchProblem

class CanibalesLikeProblem(SearchProblem):
    def __init__(self, M=3, C=3):
        # M = Cientificos, C = Muestras
        self.M = M
        self.C = C

        # Estado cientificos_izq, muestras_izq, bote_izq
        # bote_izq: 1 si el bote está a la izquierda u orilla A, 0 si está a la derecha u orilla B
        self.start = (M, C, 1)
        self.goal = (0, 0, 0)

        # Posibles movimientos del bote, es decir cuántos científicos/muestras viajan
        # Capacidad de 1 o 2 personas
        self.movimientos = [
            (1, 0),  # 1 Cientifico
            (2, 0),  # 2 Científicos
            (0, 1),  # 1 Muestra
            (0, 2),  # 2 Muestras
            (1, 1),  # 1 Cientifico y 1 Muestra
        ]

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    def es_estado_valido(self, state):
        m_izq, c_izq, bote_izq = state

        # no pueden haber cantidades negativas ni mayores al total en la orilla
        if m_izq < 0 or c_izq < 0 or m_izq > self.M or c_izq > self.C:
            return False

        # calculamos los que estan en la orilla derecha
        m_der = self.M - m_izq
        c_der = self.C - c_izq

        # restriccion en orilla izquierda, si hay cientificos, las muestras no pueden superarlos
        if m_izq > 0 and c_izq > m_izq:
            return False

        # restricción en orilla derecha, si hay cientificos, las muestras no pueden superarlos
        if m_der > 0 and c_der > m_der:
            return False

        return True

    def getSuccessors(self, state):
        sucesores = []
        m_izq, c_izq, bote_izq = state

        for dm, dc in self.movimientos:
            if bote_izq == 1:
                # el bote viaja de Izquierda a Derecha, o de orilla A a orilla B
                nuevo_m_izq = m_izq - dm
                nuevo_c_izq = c_izq - dc
                nuevo_bote = 0
                accion = f"Mover {dm} Científicos y {dc} Muestras a la orilla B"
            else:
                # el bote viaja de Derecha a Izquierda o de orilla B a orilla A
                nuevo_m_izq = m_izq + dm
                nuevo_c_izq = c_izq + dc
                nuevo_bote = 1
                accion = f"Mover {dm} Científicos y {dc} Muestras a la orilla A"

            nuevo_estado = (nuevo_m_izq, nuevo_c_izq, nuevo_bote)

            # si el estado resultante es valido, lo agregamos a los siguientes
            if self.es_estado_valido(nuevo_estado):
                sucesores.append((nuevo_estado, accion, 1))

        return sucesores

    def getCostOfActions(self, actions):
        # costo por cruce
        return len(actions)