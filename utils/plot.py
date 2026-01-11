import matplotlib.pyplot as plt
from pymoo.core.result import Result
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

    plt.savefig(f"./resources/output/instances/vrp-{ref}.png", dpi=300)
    plt.close()


def plot_pareto_frontier(res: Result, ref: str):
    plt.scatter(res.F[:, 0], res.F[:, 1])
    plt.xlabel("Distância total")
    plt.ylabel("Makespan")
    plt.savefig(f"./resources/output/pareto/frontier-{ref}.png")


def plot_solution_routes(vrp: VrpNotation, routes: list[list[int]], ref: str):
    plt.figure()

    for i, (x, y) in vrp.nodes.items():
        if i == vrp.depot:
            plt.scatter(x, y, marker="s", c="tab:orange")
            plt.text(x + 0.1, y + 0.1, str(i), fontsize=8)
        else:
            plt.scatter(x, y, c="tab:blue")
            plt.text(x + 0.1, y + 0.1, str(i), fontsize=8)

    for route in routes:
        full_route = [vrp.depot] + route + [vrp.depot]

        for i in range(len(full_route) - 1):
            x1, y1 = vrp.nodes[full_route[i]]
            x2, y2 = vrp.nodes[full_route[i + 1]]
            dx = x2 - x1
            dy = y2 - y1

            plt.quiver(
                x1, y1, dx, dy,
                angles="xy",
                scale_units="xy",
                scale=1,
                width=0.003,
                headwidth=5,
                headlength=6,
                headaxislength=5
            )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Rotas VRP")

    plt.savefig(f"./resources/output/routes/route-{ref}.png", dpi=300)
    plt.close()
