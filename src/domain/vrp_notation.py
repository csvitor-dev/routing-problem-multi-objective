from typing import Self


class VrpNotation:
    def __init__(self, dimension_capacity_line: str, depot: str) -> None:
        self.dimension, self.capacity = self.__resolve_base_instance_data(
            dimension_capacity_line)
        self.depot = int(depot)
        self.nodes: dict[int, tuple[int, int]] = {}
        self.demands: dict[int, int] = {}

    def __resolve_base_instance_data(self, dimension_capacity_line: str) -> tuple[int, int]:
        values = list(map(int, dimension_capacity_line.split(';')))
        return values[0], values[1]

    def make_nodes(self, raw_nodes: list[str]) -> Self:
        for node in raw_nodes:
            parts = node.split(';')
            self.nodes[int(parts[0])] = (int(parts[1]), int(parts[2]))
        return self

    def make_demands(self, raw_demands: list[str]) -> Self:
        for demand in raw_demands:
            parts = demand.split(';')
            self.demands[int(parts[0])] = int(parts[1])
        return self

    def __repr__(self) -> str:
        return f"""< dimension={self.dimension} capacity={self.capacity} demands={self.demands} nodes={self.nodes} >"""


# DIMENSION : 6
# CAPACITY : 7

# NODE_COORD_SECTION
# 0 0.0 0.0
# 1 2.0 3.0
# 2 5.0 4.0
# 3 1.0 6.0
# 4 6.0 1.0
# 5 3.0 7.0
# 6 7.0 5.0

# DEMAND_SECTION
# 1 2
# 2 3
# 3 2
# 4 4
# 5 2
# 6 3

# DEPOT_SECTION
# 0
