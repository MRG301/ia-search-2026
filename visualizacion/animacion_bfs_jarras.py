# visualizacion/animacion_bfs_jarras.py
# ------------------------------------
# Animación interactiva paso a paso de BFS para el Problema de las Jarras.
#
# Ejecutar desde la raíz del proyecto:
#   python -m visualizacion.animacion_bfs_jarras
#
# Controles teclado (la ventana debe tener el foco):
#   → o d : siguiente paso
#   ← o a : paso anterior
#   Espacio: play/pausa
#   Home  : ir al inicio
#   End   : ir al final
#
# Botones y slider incluidos.

from collections import deque

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
import numpy as np

from problems.jarras import JarrasProblem

def to_offsets(points):
    """
    Devuelve un np.array de forma (N,2). Si no hay puntos, (0,2).
    Esto evita el error de Matplotlib cuando la lista está vacía.
    """
    clean = []
    for p in points:
        if isinstance(p, tuple) and len(p) == 2:
            clean.append([p[0], p[1]])

    if len(clean) == 0:
        return np.empty((0, 2), dtype=float)

    return np.array(clean, dtype=float)
    

def bfs_con_traza(problem):
    """
    BFS que guarda snapshots por iteración:
      - actual: estado que se expande
      - frontera: cola (lista de estados)
      - visitados: set de estados
      - accion_entrada: acción usada para llegar al estado actual (None para inicio)
    Además guarda padre/acción para reconstruir el camino.
    """
    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return [], [inicio], [], {inicio: None}

    cola = deque([inicio])
    visitados = set([inicio])

    padre = {inicio: None}
    accion_aqui = {inicio: None}
    accion_entrada = {inicio: None}

    traza = []

    while cola:
        estado_actual = cola.popleft()

        traza.append({
            "actual": estado_actual,
            "accion_entrada": accion_entrada.get(estado_actual),
            "frontera": list(cola),
            "visitados": set(visitados),
        })

        if problem.isGoalState(estado_actual):
            break

        for sucesor, accion, costo in problem.getSuccessors(estado_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                padre[sucesor] = estado_actual
                accion_aqui[sucesor] = accion
                accion_entrada[sucesor] = accion
                cola.append(sucesor)

    meta = problem.goal
    if meta not in padre:
        return [], [], traza, padre

    # Reconstrucción del camino (estados)
    estados_camino = []
    s = meta
    while s is not None:
        estados_camino.append(s)
        s = padre[s]
    estados_camino.reverse()

    # Reconstrucción de acciones
    acciones_camino = []
    for i in range(1, len(estados_camino)):
        acciones_camino.append(accion_aqui[estados_camino[i]])

    return acciones_camino, estados_camino, traza, padre


def animar_bfs_jarras(problem, intervalo_ms=450, mostrar_cola_max=18):
    acciones, estados_camino, traza, _padre = bfs_con_traza(problem)

    if not traza:
        print("No hay traza (¿inicio ya era meta?).")
        return

    # Todos los estados posibles
    todos = [(a, b) for a in range(problem.capA + 1) for b in range(problem.capB + 1)]

    # -------- Layout PRO: dos paneles
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1.0])

    ax_states = fig.add_subplot(gs[0, 0])
    ax_info = fig.add_subplot(gs[0, 1])
    ax_info.axis("off")

    ax_states.set_title("BFS paso a paso — Espacio de estados (a,b)")
    ax_states.set_xlabel("Litros en jarra A")
    ax_states.set_ylabel("Litros en jarra B")
    ax_states.set_xlim(-0.5, problem.capA + 0.5)
    ax_states.set_ylim(-0.5, problem.capB + 0.5)
    ax_states.set_xticks(range(problem.capA + 1))
    ax_states.set_yticks(range(problem.capB + 1))
    ax_states.grid(True, alpha=0.25)

    # Base: estados posibles
    ax_states.scatter(
        [s[0] for s in todos],
        [s[1] for s in todos],
        s=260, alpha=0.12, label="Estados posibles"
    )

    puntos_visitados = ax_states.scatter([], [], s=260, alpha=0.55, label="Visitados")
    puntos_frontera = ax_states.scatter([], [], s=260, alpha=0.85, label="Frontera (cola)")
    punto_actual = ax_states.scatter([], [], s=360, marker="*", label="Actual")
    puntos_camino = ax_states.scatter([], [], s=300, alpha=0.90, label="Camino solución")

    ax_states.scatter([problem.start[0]], [problem.start[1]], s=380, marker="s", label="Inicio")
    ax_states.scatter([problem.goal[0]], [problem.goal[1]], s=380, marker="X", label="Meta")
    ax_states.legend(loc="upper left")

    # -------- Dibujo PRO de jarras
    jarA_outline = plt.Rectangle((0.10, 0.20), 0.25, 0.60, fill=False, linewidth=2)
    jarB_outline = plt.Rectangle((0.55, 0.20), 0.25, 0.60, fill=False, linewidth=2)
    ax_info.add_patch(jarA_outline)
    ax_info.add_patch(jarB_outline)

    jarA_fill = plt.Rectangle((0.10, 0.20), 0.25, 0.00, alpha=0.35)
    jarB_fill = plt.Rectangle((0.55, 0.20), 0.25, 0.00, alpha=0.35)
    ax_info.add_patch(jarA_fill)
    ax_info.add_patch(jarB_fill)

    text_title = ax_info.text(0.02, 0.98, "", va="top", fontsize=12, fontweight="bold")
    text_status = ax_info.text(0.02, 0.86, "", va="top", fontsize=11)
    text_queue = ax_info.text(0.02, 0.54, "", va="top", fontsize=10, family="monospace")
    text_action = ax_info.text(0.02, 0.12, "", va="top", fontsize=11)

    # -------- Controles
    fig.subplots_adjust(bottom=0.22)

    ax_btn_prev2 = fig.add_axes([0.10, 0.06, 0.07, 0.06])
    ax_btn_prev  = fig.add_axes([0.18, 0.06, 0.07, 0.06])
    ax_btn_play  = fig.add_axes([0.26, 0.06, 0.07, 0.06])
    ax_btn_next  = fig.add_axes([0.34, 0.06, 0.07, 0.06])
    ax_btn_next2 = fig.add_axes([0.42, 0.06, 0.07, 0.06])

    btn_prev2 = Button(ax_btn_prev2, "⏮︎")
    btn_prev  = Button(ax_btn_prev,  "◀")
    btn_play  = Button(ax_btn_play,  "⏯")
    btn_next  = Button(ax_btn_next,  "▶")
    btn_next2 = Button(ax_btn_next2, "⏭︎")

    ax_slider = fig.add_axes([0.55, 0.08, 0.38, 0.03])
    slider = Slider(ax_slider, "Paso", 0, len(traza), valinit=0, valstep=1)

    frame_idx = 0
    playing = False

    def set_frame(i, from_slider=False):
        nonlocal frame_idx
        i = max(0, min(int(i), len(traza)))  # len(traza) es pantalla final
        frame_idx = i
        if not from_slider:
            slider.set_val(frame_idx)
        draw_frame(frame_idx)
        fig.canvas.draw_idle()

    def resumen_cola(frontera):
        # Aquí NO metemos "..." en la lista que se dibuja, solo en texto.
        if len(frontera) <= mostrar_cola_max:
            return frontera, False
        return frontera[:mostrar_cola_max], True

    def draw_frame(i):
        if i < len(traza):
            snap = traza[i]
            actual = snap["actual"]
            frontera = snap["frontera"]
            visit = snap["visitados"]
            accion_entra = snap.get("accion_entrada")

            puntos_visitados.set_offsets(to_offsets(list(visit)))
            puntos_frontera.set_offsets(to_offsets(frontera))
            punto_actual.set_offsets(to_offsets([actual]))
            puntos_camino.set_offsets(to_offsets([]))

            a, b = actual
            jarA_fill.set_height(0.60 * (a / problem.capA if problem.capA else 0))
            jarB_fill.set_height(0.60 * (b / problem.capB if problem.capB else 0))

            text_title.set_text("Estado actual (expandiendo)")
            text_status.set_text(
                f"Paso: {i+1}/{len(traza)}\n"
                f"Actual: {actual}\n"
                f"Visitados: {len(visit)}   |   Frontera: {len(frontera)}\n"
                f"Capacidades: A={problem.capA}, B={problem.capB}\n"
                f"Inicio={problem.start}   Meta={problem.goal}"
            )

            cola_muestra, recortada = resumen_cola(frontera)
            cola_txt = "\n".join(str(x) for x in cola_muestra)
            if recortada:
                cola_txt += "\n..."
            text_queue.set_text("Cola (frontera) [primeros]:\n" + cola_txt)

            text_action.set_text(
                "Acción para llegar aquí: " + ("(inicio)" if accion_entra is None else str(accion_entra))
            )

        else:
            # Pantalla final: camino solución
            puntos_visitados.set_offsets(to_offsets([]))
            puntos_frontera.set_offsets(to_offsets([]))
            punto_actual.set_offsets(to_offsets([]))
            puntos_camino.set_offsets(to_offsets(estados_camino))

            if estados_camino:
                a, b = estados_camino[-1]
                jarA_fill.set_height(0.60 * (a / problem.capA if problem.capA else 0))
                jarB_fill.set_height(0.60 * (b / problem.capB if problem.capB else 0))

            text_title.set_text("✅ BFS terminó — Camino solución")
            text_status.set_text(
                f"Expansiones BFS: {len(traza)}\n"
                f"Longitud solución (acciones): {len(acciones)}\n"
                f"Inicio={problem.start}   Meta={problem.goal}"
            )
            text_queue.set_text("Camino (estados):\n" + "\n".join(str(x) for x in estados_camino))
            text_action.set_text("Camino (acciones):\n" + "\n".join(str(a) for a in acciones))

    # Inicial
    draw_frame(0)

    # Botones
    def on_prev2(_): set_frame(0)
    def on_prev(_):  set_frame(frame_idx - 1)
    def on_play(_):
        nonlocal playing
        playing = not playing
    def on_next(_):  set_frame(frame_idx + 1)
    def on_next2(_): set_frame(len(traza))

    btn_prev2.on_clicked(on_prev2)
    btn_prev.on_clicked(on_prev)
    btn_play.on_clicked(on_play)
    btn_next.on_clicked(on_next)
    btn_next2.on_clicked(on_next2)

    # Slider
    def on_slider(val):
        set_frame(int(val), from_slider=True)
    slider.on_changed(on_slider)

    # Teclado
    def on_key(event):
        nonlocal playing
        if event.key in ("right", "d"):
            set_frame(frame_idx + 1)
        elif event.key in ("left", "a"):
            set_frame(frame_idx - 1)
        elif event.key == " ":
            playing = not playing
        elif event.key == "home":
            set_frame(0)
        elif event.key == "end":
            set_frame(len(traza))

    fig.canvas.mpl_connect("key_press_event", on_key)

    # Timer/play
    def tick(_):
        nonlocal frame_idx, playing
        if playing:
            if frame_idx < len(traza):
                set_frame(frame_idx + 1)
            else:
                playing = False

    _anim = FuncAnimation(fig, tick, interval=intervalo_ms)
    plt.show()


if __name__ == "__main__":
    problema = JarrasProblem(capA=4, capB=3, start=(0, 0), goal=(2, 0))
    animar_bfs_jarras(problema, intervalo_ms=450)