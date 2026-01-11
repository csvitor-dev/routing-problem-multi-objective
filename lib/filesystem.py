from pathlib import Path
from os import path


def read_file(path: Path) -> list[str]:
    with open(path, 'r') as file:
        mapping = map(lambda line: line.replace('\n', ''), file.readlines())
        return list(filter(lambda line: line != '', mapping))


def resolve_path(base_path: str, fileName: str) -> Path:
    abs_path = path.abspath(f'{base_path}/{fileName}')
    target_path = Path(abs_path)

    if target_path.exists() is False:
        raise FileExistsError
    return target_path
