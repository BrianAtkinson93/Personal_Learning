# 1. Multiplication and Exponentiation
def multiplication_and_exponentiation():
    """
    Demonstrates the use of the asterisk (*) for multiplication and exponentiation.
    """
    # Multiplication
    result_mul = 5 * 3
    print(f"Multiplication result: {result_mul}")  # Output: 15

    # Exponentiation
    result_exp = 2 ** 3
    print(f"Exponentiation result: {result_exp}")  # Output: 8


# 2. Unpacking Sequences
def unpacking_sequences():
    """
    Demonstrates the use of the asterisk (*) for unpacking sequences like lists or tuples.
    """
    # Unpacking lists
    first, *rest = [1, 2, 3, 4]
    print(f"First: {first}, Rest: {rest}")  # Output: First: 1, Rest: [2, 3, 4]

    # Unpacking in function arguments
    def func(first, *rest):
        print(f"First: {first}, Rest: {rest}")

    func(1, 2, 3, 4)


# 3. Extended Unpacking in Function Calls
def extended_unpacking_in_function_calls():
    """
    Demonstrates the use of the asterisk (*) to unpack a sequence and pass its elements as positional arguments to a function.
    """

    def sum_three_numbers(a, b, c):
        return a + b + c

    numbers = [1, 2, 3]
    result = sum_three_numbers(*numbers)
    print(f"Result of sum_three_numbers: {result}")  # Output: 6


# 4. Keyword Argument Unpacking (**)
def keyword_argument_unpacking():
    """
    Demonstrates the use of double asterisks (**) to unpack a dictionary and pass its key-value pairs as keyword arguments to a function.
    """

    def greet(name, age):
        print(f"Hello, {name}. You are {age} years old.")

    info = {'name': 'John', 'age': 30}
    greet(**info)


# 5. Using * in Function Definitions for *args
def using_star_in_function_definitions_for_args():
    """
    Demonstrates the use of a single asterisk (*) before a parameter in function definitions to collect all extra positional arguments into a tuple.
    """

    def func_with_args(*args):
        for arg in args:
            print(arg)

    func_with_args(1, 2, 3, 4)


# 6. Using ** in Function Definitions for **kwargs
def using_double_star_in_function_definitions_for_kwargs():
    """
    Demonstrates the use of double asterisks (**) before a parameter in function definitions to collect all extra keyword arguments into a dictionary.
    """

    def func_with_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    func_with_kwargs(a=1, b=2, c=3)


# 7. Repetition Operator for Sequences
def repetition_operator_for_sequences():
    """
    Demonstrates the use of the asterisk (*) as a repetition operator for sequences like lists and strings.
    """
    # Repeat a list
    repeated_list = [1, 2] * 3
    print(f"Repeated list: {repeated_list}")  # Output: [1, 2, 1, 2, 1, 2]

    # Repeat a string
    repeated_str = "AB" * 3
    print(f"Repeated string: {repeated_str}")  # Output: "ABABAB"


if __name__ == "__main__":
    print("1. Multiplication and Exponentiation")
    multiplication_and_exponentiation()
    print("\n2. Unpacking Sequences")
    unpacking_sequences()
    print("\n3. Extended Unpacking in Function Calls")
    extended_unpacking_in_function_calls()
    print("\n4. Keyword Argument Unpacking")
    keyword_argument_unpacking()
    print("\n5. Using * in Function Definitions for *args")
    using_star_in_function_definitions_for_args()
    print("\n6. Using ** in Function Definitions for **kwargs")
    using_double_star_in_function_definitions_for_kwargs()
    print("\n7. Repetition Operator for Sequences")
    repetition_operator_for_sequences()
