import itertools


def demo_count():
    """
    Demonstrates the use of itertools.count.
    Generates numbers starting from `start` and incrementing by `step`.
    """
    print("=== count ===")
    for num in itertools.count(start=5, step=5):
        if num > 20:
            break
        print(num)


def demo_cycle():
    """
    Demonstrates the use of itertools.cycle.
    Cycles infinitely over the given iterable.
    """
    print("\n=== cycle ===")
    i = 0
    for item in itertools.cycle("ABC"):
        if i > 5:
            break
        print(item)
        i += 1


def demo_repeat():
    """
    Demonstrates the use of itertools.repeat.
    Repeats an element for a specified number of times.
    """
    print("\n=== repeat ===")
    for item in itertools.repeat("A", 3):
        print(item)


def demo_chain():
    """
    Demonstrates the use of itertools.chain.
    Chains multiple iterables together.
    """
    print("\n=== chain ===")
    for item in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
        print(item)


def demo_combinations():
    """
    Demonstrates the use of itertools.combinations.
    Generates all possible r-length combinations of elements from the iterable.
    """
    print("\n=== combinations ===")
    for combo in itertools.combinations("ABC", 2):
        print(combo)


def demo_permutations():
    """
    Demonstrates the use of itertools.permutations.
    Generates all possible r-length permutations of elements from the iterable.
    """
    print("\n=== permutations ===")
    for perm in itertools.permutations("ABC", 2):
        print(perm)


def demo_product():
    """
    Demonstrates the use of itertools.product.
    Generates the Cartesian product of the provided iterables.
    """
    print("\n=== product ===")
    for item in itertools.product([1, 2], ['a', 'b']):
        print(item)


def demo_zip_longest():
    """
    Demonstrates the use of itertools.zip_longest.
    Zips iterables and fills in missing values with `fillvalue`.
    """
    print("\n=== zip_longest ===")
    for item in itertools.zip_longest([1, 2], ['a'], fillvalue=None):
        print(item)


def demo_islice():
    """
    Demonstrates the use of itertools.islice.
    Slices an iterable from `start` to `stop` with a step of `step`.
    """
    print("\n=== islice ===")
    for item in itertools.islice(range(10), 0, 10, 2):
        print(item)


def demo_filterfalse():
    """
    Demonstrates the use of itertools.filterfalse.
    Filters elements from `iterable` for which `predicate` returns False.
    """
    print("\n=== filterfalse ===")
    for item in itertools.filterfalse(lambda x: x % 2 == 0, range(5)):
        print(item)


if __name__ == "__main__":
    demo_count()
    demo_cycle()
    demo_repeat()
    demo_chain()
    demo_combinations()
    demo_permutations()
    demo_product()
    demo_zip_longest()
    demo_islice()
    demo_filterfalse()
