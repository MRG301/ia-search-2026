# visualizacion.py
# ----------------
# Visualización del espacio de estados del problema de las jarras

import networkx as nx
import matplotlib.pyplot as plt
from problems.jarras import JarrasProblem


def construir_grafo(problema):
    """
    Construye el grafo completo del espacio de estados.
    """
    G = nx.DiGraph()

    visitados = set()
    frontera = [problema.getStartState()]

    while frontera:
        estado = frontera.pop(0)

        if estado in visitados:
            continue

        visitados.add(estado)

        for sucesor, accion, costo in problema.getSuccessors(estado):
            G.add_edge(estado, sucesor, label=accion)
            if sucesor not in visitados:
                frontera.append(sucesor)

    return G


def dibujar_grafo(G):
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue")

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Espacio de Estados - Problema de las Jarras")
    plt.show()


if __name__ == "__main__":
    problema = JarrasProblem(capA=4, capB=3)
    G = construir_grafo(problema)
    dibujar_grafo(G)