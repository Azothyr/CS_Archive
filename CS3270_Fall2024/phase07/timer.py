import time
from functools import wraps
from typing import Optional, Any


def function_timer(timer_attr: Optional[str] = None) -> callable:
    """
    Decorator that measures the execution time of a function or method.

    Parameters:
        timer_attr (Optional[str]): Name of the attribute to set the elapsed time.
                                    If not provided, elapsed time is printed or returned.
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time: float = time.time()
            result: Any = func(*args, **kwargs)
            elapsed_time: float = time.time() - start_time

            # If `timer_attr` is provided and the first argument is `self`, set the time on the attribute.
            if timer_attr and len(args) > 0:
                instance = args[0]
                # Check if the first argument has the attribute (likely `self`).
                if hasattr(instance, timer_attr):
                    setattr(instance, timer_attr, elapsed_time)
                else:
                    print(f"Warning: {instance} does not have attribute '{timer_attr}' to store elapsed time.")
            else:
                print(f"Elapsed time for {func.__name__}: {elapsed_time:.4f} seconds")
            return result

        return wrapper

    return decorator
