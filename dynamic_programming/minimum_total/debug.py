from functools import wraps
from typing import List, Callable
from pprint import pp


class Tracker:
    def __init__(self):
        self.call_stack: List[dict] = []

    def track(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                self.call_stack.append({
                    "fn": func.__name__,
                    "args": args,
                    # "kwargs": kwargs,
                    "depth": len(self.call_stack),
                })
                result = func(*args, **kwargs)
                pp(dict(stack=self.call_stack, result=result))

                return result
            finally:
                self.call_stack.pop()

        return wrapper
