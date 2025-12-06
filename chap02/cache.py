import functools
import time


def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args,**kwargs)
        return function._cache[key]
    return wrapper

@memoize
def long_operation(x, y):
    time.sleep(5)   # Or some other suitable long expression.
    return x + y

if __name__ == "__main__":
    print(long_operation(3,5))
    print(long_operation(3,5))
    print(long_operation(5,3))
    print(long_operation(5,3))
