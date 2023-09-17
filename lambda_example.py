def demo_simple_lambda():
    """
    Demonstrates a simple lambda function that adds two numbers.
    """
    print("=== Simple Lambda ===")
    add = lambda x, y: x + y
    print(add(5, 3))  # Output: 8


def demo_map_lambda():
    """
    Demonstrates the use of lambda with the map function.
    Squares each element in the list.
    """
    print("\n=== Map with Lambda ===")
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]


def demo_filter_lambda():
    """
    Demonstrates the use of lambda with the filter function.
    Filters out odd numbers from the list.
    """
    print("\n=== Filter with Lambda ===")
    numbers = [1, 2, 3, 4]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(even)  # Output: [2, 4]


def demo_sort_lambda():
    """
    Demonstrates the use of lambda with the sorted function.
    Sorts a list of tuples based on the second element.
    """
    print("\n=== Sort with Lambda ===")
    pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    print(sorted_pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


def demo_max_lambda():
    """
    Demonstrates the use of lambda with the max function.
    Finds the longest word in the list.
    """
    print("\n=== Max with Lambda ===")
    words = ['apple', 'banana', 'cherry']
    longest_word = max(words, key=lambda x: len(x))
    print(longest_word)  # Output: 'banana'


def demo_multiple_args_lambda():
    """
    Demonstrates a lambda function that takes multiple arguments.
    Multiplies two numbers and adds the third.
    """
    print("\n=== Lambda with Multiple Arguments ===")
    func = lambda x, y, z: x * y + z
    print(func(2, 3, 1))  # Output: 7


def demo_higher_order_lambda():
    """
    Demonstrates a higher-order lambda function.
    Returns a lambda function that multiplies its argument by `n`.
    """
    print("\n=== Higher-Order Lambda ===")
    multiplier = lambda n: lambda x: x * n
    times_two = multiplier(2)
    print(times_two(4))  # Output: 8

    points2D = [(1, 2), (15, 1), (5, - 1), (10, 4)]
    points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
    print(points2D)
    print(points2D_sorted)


if __name__ == "__main__":
    demo_simple_lambda()
    demo_map_lambda()
    demo_filter_lambda()
    demo_sort_lambda()
    demo_max_lambda()
    demo_multiple_args_lambda()
    demo_higher_order_lambda()
