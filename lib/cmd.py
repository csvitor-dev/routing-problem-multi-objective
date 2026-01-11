import sys
from typing import Any


def pluck_flags_from_cmd_args(search_for: list[str]) -> dict[str, Any]:
    args = __map_args(sys.argv[1:])

    if len(args) == 0:
        raise ValueError('The flags need to be provided.')
    return {target: args[target] if target in args else False for target in search_for}


def __map_args(raw_args: list[str]) -> dict[str, Any]:
    filtering = filter(lambda arg: arg.isdigit()
                       is False and '--' in arg, raw_args)
    mapping = list(map(lambda arg: arg.replace(
        '--', '').split('='), filtering))
    output_mapper: dict[str, Any] = {}

    for parts in mapping:
        if len(parts) == 1:
            output_mapper[parts[0]] = True
        else:
            output_mapper[parts[0]] = parts[1]
    return output_mapper
