from lib.filesystem import read_file, resolve_path
from src.domain.vrp_notation import VrpNotation


def get_instance(ref: str) -> VrpNotation:
    file = resolve_path(
        './resources/vrp', f'instance-{ref}.vrp')
    raw = read_file(file)
    vrp = VrpNotation(raw[0], raw[len(raw)-1])

    return vrp.make_nodes(raw[1:vrp.dimension+2]).make_demands(raw[vrp.dimension+2:len(raw)-1])
