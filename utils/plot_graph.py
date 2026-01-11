import matplotlib.pyplot as plt
from src.domain.vrp_notation import VrpNotation


def plot_vrp_instance(vrp: VrpNotation, ref: str):
    xs: list[int] = []
    ys: list[int] = []

    for i, (x, y) in vrp.nodes.items():
        xs.append(x)
        ys.append(y)

    depot_x, depot_y = vrp.nodes[vrp.depot]

    plt.figure()
    plt.scatter(xs, ys)
    plt.scatter(depot_x, depot_y, marker="s")

    for i, (x, y) in vrp.nodes.items():
        plt.text(x + 0.1, y + 0.1, str(i), fontsize=8)

    plt.title("Instância VRP")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.savefig(f"./resources/output/vrp_instance_{ref}.png", dpi=300)
    plt.close()
