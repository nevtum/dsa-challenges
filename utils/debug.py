from functools import wraps
from pprint import pp


class CallTracker:
    def __init__(self, use_breakpoint=False):
        self.call_stack = []
        self.use_breakpoint = use_breakpoint

    def track(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.call_stack.append(
                    {
                        "fn": func.__name__,
                        "args": args,
                        # "kwargs": kwargs,
                        "depth": len(self.call_stack),
                    }
                )
                result = func(*args, **kwargs)
                pp(dict(stack=self.call_stack, result=result))
                if self.use_breakpoint:
                    breakpoint()

                return result
            finally:
                self.call_stack.pop()

        return wrapper
