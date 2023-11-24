from typing import Any, Callable
from datetime import datetime


class Timeit:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.timed = []

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start = datetime.now()
        res = self.fun(*args, **kwds)
        end = datetime.now()
        print(end-start)
        self.timed.append(end - start)
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Took {self.timed} seconds")