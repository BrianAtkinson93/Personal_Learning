import sys
import time


def simple_generator():
    """
    A simple generator function that yields numbers from 0 to 4.
    """
    for i in range(5):
        yield i


def fibonacci_generator(n):
    """
    A generator function that yields Fibonacci numbers up to the nth element.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def generator_expression():
    """
    Demonstrates the use of a generator expression.
    Similar to list comprehension but produces a generator.
    """
    return (x * x for x in range(5))


def infinite_generator():
    """
    An infinite generator function that keeps yielding the word 'infinite'.
    """
    while True:
        yield 'infinite'


def generator_with_value():
    """
    A generator function that receives a value using the `send` method.
    """
    received = yield "Ready to receive"
    while received:
        received = yield f"Received: {received}"


# Reading a large file line-by-line
def read_large_file(file_path):
    """
    Generators compute values on-the-fly and yield them one at a time, consuming less memory. This is useful when
    working with large data sets.
    :param file_path:
    :return: yield
    """
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("=== Simple Generator ===")
    for num in simple_generator():
        print(num)

    print("\n=== Fibonacci Generator ===")
    for num in fibonacci_generator(10):
        print(num)

    print("\n=== Generator Expression ===")
    gen_expr = generator_expression()
    for num in gen_expr:
        print(num)

    print("\n=== Infinite Generator ===")
    infinite_gen = infinite_generator()
    for i, val in enumerate(infinite_gen):
        if i >= 5:
            break
        print(val)

    print("\n=== Generator with Value ===")
    gen_val = generator_with_value()
    print(next(gen_val))  # Output: "Ready to receive"
    print(gen_val.send("Hello"))  # Output: "Received: Hello"
    print(gen_val.send("World"))  # Output: "Received: World"
    print(gen_val.send('Another'))

    print("\n === Generator first n ===")
    print(sum(firstn(100000)))
    print(sum(list(firstn_gen(100000))))
    print(sys.getsizeof(firstn(10000000)))
    print(sys.getsizeof(firstn_gen(10000000)))

    print('\n === fib ===')
    fib = fibonacci(300)
    # print(list(fib))
    for i in fib:
        print(i)

    print(f'\n === generator lists ===')


    def bytes_to_megabytes(bytes_value):
        return bytes_value / (1024 ** 2)


    def bytes_to_gigabytes(bytes_value):
        return bytes_value / (1024 ** 3)

    start_time = time.time()
    mygenerator = (i for i in range(1000000000) if i % 2 == 0)
    # mygenerator = (i for i in range(100) if i % 2 == 0)
    print(f'sum : {sum(mygenerator)}')
    print(f"{sys.getsizeof(mygenerator)} bytes")
    print(f"{sys.getsizeof(mygenerator) * 8} bits")
    print(f"{bytes_to_megabytes(sys.getsizeof(mygenerator))} MB")
    print(f"{bytes_to_gigabytes(sys.getsizeof(mygenerator))} GB")
    end_time = time.time()
    print(f'Total time: {end_time - start_time}')

    print()
    start_time = time.time()
    mygenerator2 = [i for i in range(1000000000) if i % 2 == 0]
    # mygenerator2 = [i for i in range(100) if i % 2 == 0]
    print(f'sum : {sum(mygenerator2)}')
    print(f'{sys.getsizeof(mygenerator2)} bytes')
    print(f'{sys.getsizeof(mygenerator2) * 8} bits')
    print(f"{bytes_to_megabytes(sys.getsizeof(mygenerator2))} MB")
    print(f"{bytes_to_gigabytes(sys.getsizeof(mygenerator2))} GB")

    end_time = time.time()
    print(f'Total time: {end_time - start_time}')
