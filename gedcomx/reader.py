from pathlib import Path
from typing import Union


class Reader:
    def __init__(self, path: Union[Path, str], *args, **kwargs):
        path = Path(path)


class Writer:
    def __init__(self, path: Union[Path, str], *args, **kwargs):
        path = Path(path)
