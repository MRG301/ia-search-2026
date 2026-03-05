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

class CanibalesLikeProblem:
    def __init__(self, M=3, C=3):
        self.M = M
        self.C = C

        # Estado: (m_izq, c_izq, bote_izq)
        # bote_izq: 1 si el bote está a la izquierda, 0 si está a la derecha
        self.start = (M, C, 1)
        self.goal = (0, 0, 0)

        # Posibles movimientos del bote (cuántos misioneros/caníbales viajan)
        # Capacidad de 1 o 2 personas
        self.movimientos = [
            (1, 0),  # 1 M
            (2, 0),  # 2 M
            (0, 1),  # 1 C
            (0, 2),  # 2 C
            (1, 1),  # 1 M y 1 C
        ]

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    # -------------------------
    # Helpers recomendados
    # -------------------------

    def es_estado_valido(self, state):
        """
        TODO (ESTUDIANTES):
        Regresar True si el estado cumple:
        - 0 <= m_izq <= M, 0 <= c_izq <= C
        - En la orilla izquierda: si m_izq > 0 entonces m_izq >= c_izq
        - En la orilla derecha: m_der = M - m_izq, c_der = C - c_izq
          si m_der > 0 entonces m_der >= c_der
        """
        util = True  # <-- reemplazar
        return util

    def getSuccessors(self, state):
        """
        TODO (ESTUDIANTES):
        Debe regresar lista de (sucesor, accion, costo)

        Reglas:
        - Si bote_izq == 1, el bote cruza de izquierda a derecha:
            (m_izq - dm, c_izq - dc, 0)
        - Si bote_izq == 0, cruza de derecha a izquierda:
            (m_izq + dm, c_izq + dc, 1)
        - Solo permitir movimientos donde:
            - dm + dc es 1 o 2
            - No se transporta gente "negativa"
            - El estado resultante sea válido (es_estado_valido)
        """
        sucesores = []

        # TODO: implementar transiciones para cada movimiento permitido
        # y agregar a sucesores:
        # sucesores.append((nuevo_estado, "Acción descriptiva", 1))

        return sucesores

    def getCostOfActions(self, actions):
        # Costo 1 por cruce
        return len(actions)