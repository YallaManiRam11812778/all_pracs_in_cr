from functools import wraps
from typing import Callable, Any
import time

def calculating_execution_time(func:Callable) -> Callable :
    @wraps(func)
    def wrapper_func(*args, **kwargs) -> Any:
        start_time : float = time.perf_counter()
        result : Any = func(*args, **kwargs)
        end_time : float = time.perf_counter()
        message : str =  f"Execution time taken for '{func.__name__}' is {end_time - start_time:.2f} seconds"
        return message
    return wrapper_func

@calculating_execution_time
def main():
    time.sleep(2.24)
main()
