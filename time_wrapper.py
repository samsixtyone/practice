
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end   = time.perf_counter()
        print (f"Function {func.__name__} took {end - start:.6f} seconds to execute")
        return result
    return wrapper

@timeit
def slow_func():
    time.sleep(2)

slow_func()

