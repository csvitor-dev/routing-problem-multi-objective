from pymoo.core.problem import ElementwiseProblem
import numpy as np
from math import sqrt
from typing import Any
from src.domain.vrp_notation import VrpNotation


class DomainProblem(ElementwiseProblem):
    def __init__(self, vrp: VrpNotation):
        self.coords = vrp.nodes
        self.demands = vrp.demands
        self.capacity = vrp.capacity
        self.depot = vrp.depot

        super().__init__(
            n_var=vrp.dimension,
            n_obj=2,
            xl=0.0,
            xu=1.0,
            type_var=float
        )

    def __decode(self, x: list[float]) -> list[list[int]]:
        permutation = [v + 1 for v in np.argsort(x)]
        routes: list[list[int]] = []
        current_route = []
        load = 0

        for client in permutation:
            if load + self.demands[client] <= self.capacity:
                current_route.append(client)
                load += self.demands[client]
            else:
                routes.append(current_route)
                current_route = [client]
                load = self.demands[client]
        routes.append(current_route)
        return routes

    def __distance(self, i: int, j: int) -> float:
        x_diff_ij = self.coords[i][0] - self.coords[j][0]
        y_diff_ij = self.coords[i][1] - self.coords[j][1]

        return sqrt(x_diff_ij**2 + y_diff_ij**2)

    def _evaluate(self, x: list[float], out: dict[str, Any], *args, **kwargs):
        routes = self.__decode(x)
        total_distance = 0
        max_route_distance = 0

        for route in routes:
            dist = self.__distance(self.depot, route[0])

            for i in range(len(route) - 1):
                dist += self.__distance(route[i], route[i+1])
            dist += self.__distance(route[-1], self.depot)
            total_distance += dist
            max_route_distance = max(max_route_distance, dist)
        out["F"] = [total_distance, max_route_distance]
