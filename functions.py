# Function Basics
def basic_function():
    """
    A basic function with no arguments and no return value.
    """
    print("This is a basic function.")


# Function with Positional Arguments
def positional_arguments(a, b, c):
    """
    A function with positional arguments.
    The values for a, b, and c must be provided in the order they are defined.
    """
    print(f"a: {a}, b: {b}, c: {c}")


# Function with Default Arguments
def default_arguments(a, b=5, c=10):
    """
    A function with default arguments.
    Default values are provided for b and c.
    """
    print(f"a: {a}, b: {b}, c: {c}")


# Function with Keyword Arguments
def keyword_arguments(a, b, c):
    """
    A function that can be called with keyword arguments.
    Keyword arguments can be passed in any order.
    """
    print(f"a: {a}, b: {b}, c: {c}")


# Function with Variable-length Positional Arguments
def var_positional_args(*args):
    """
    A function that accepts a variable number of positional arguments.
    The arguments are received as a tuple.
    """
    print(f"args: {args}")


# Function with Variable-length Keyword Arguments
def var_keyword_args(**kwargs):
    """
    A function that accepts a variable number of keyword arguments.
    The arguments are received as a dictionary.
    """
    print(f"kwargs: {kwargs}")


# Function with Mixed Argument Types
def mixed_arguments(a, b, *args, keyword1=None, keyword2=None, **kwargs):
    """
    A function that demonstrates using all types of arguments.
    """
    print(f"a: {a}, b: {b}, args: {args}, keyword1: {keyword1}, keyword2: {keyword2}, kwargs: {kwargs}")


# Function Returning a Value
def return_value(a, b):
    """
    A function that returns a value.
    """
    return a + b


# Function with Docstring
def function_with_docstring():
    """
    This is a function with a docstring.
    The docstring provides information about the function.
    """
    pass


def versatile_function(**kwargs):
    """
    Executes different code blocks based on the keyword arguments provided.
    """
    if 'action' in kwargs and kwargs['action'] == 'add':
        result = kwargs.get('a', 0) + kwargs.get('b', 0)
        print(f"Result of addition: {result}")
    elif 'action' in kwargs and kwargs['action'] == 'multiply':
        result = kwargs.get('a', 1) * kwargs.get('b', 1)
        print(f"Result of multiplication: {result}")
    else:
        print("Invalid or insufficient arguments.")


if __name__ == "__main__":
    # Function Basics
    basic_function()

    # Positional Arguments
    positional_arguments(1, 2, 3)

    # Default Arguments
    default_arguments(1)
    default_arguments(1, c=20)

    # Keyword Arguments
    keyword_arguments(a=1, c=3, b=2)

    # Variable-length Positional Arguments
    var_positional_args(1, 2, 3, 4, 5)

    # Variable-length Keyword Arguments
    var_keyword_args(a=1, b=2, c=3)

    # Mixed Argument Types
    mixed_arguments(1, 2, 3, 4, 5, keyword1="hello", keyword2="world", extra1="x", extra2="y")

    # Function Returning a Value
    result = return_value(5, 10)
    print(f"Result: {result}")

    # Function with Docstring
    print(function_with_docstring.__doc__)

    versatile_function(action="add", a=5, b=3)
    versatile_function(action="multiply", a=5, b=3)
