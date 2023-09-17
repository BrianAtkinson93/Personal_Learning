from functools import wraps


def simple_decorator(func):
    """
    A simple decorator that prints a message before and after the function call.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@simple_decorator
def say_hello(name):
    """
    A simple function that takes a name and prints a greeting.
    """
    print(f"Hello, {name}!")


def start_end_decorator(func):
    def wrapper():
        print(f'Starting...')
        func()
        print(f'Finished...')

    return wrapper


@start_end_decorator
def print_name():
    print(f'Brian')


def timer_decorator(func):
    """
    A decorator that prints the time a function takes to execute.
    """
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result

    return wrapper


@timer_decorator
def slow_function(duration):
    """
    A function that simulates a long-running computation.
    """
    import time
    time.sleep(duration)


def memoize_decorator(func):
    """
    A decorator that caches the results of function calls.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize_decorator
def fibonacci(n):
    """
    A function that calculates the nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("=== Simple Decorator ===")
    say_hello("John")

    print('\n')
    print_name()
    print('\n')

    print("\n=== Timer Decorator ===")
    results = slow_function(2)
    print(results)

    print("\n=== Memoize Decorator ===")
    print(fibonacci(30))
    print(fibonacci(30))  # This call will return the cached result
