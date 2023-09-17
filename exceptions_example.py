def demo_simple_exception():
    """
    Demonstrates a simple try-except block.
    Catches a division by zero error.
    """
    print("=== Simple Exception ===")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")


def demo_multiple_exceptions():
    """
    Demonstrates handling multiple exceptions.
    Catches both division by zero and type errors.
    """
    print("\n=== Multiple Exceptions ===")
    try:
        result = 10 / 'a'
    except (ZeroDivisionError, TypeError):
        print("Invalid operation.")


def demo_exception_details():
    """
    Demonstrates how to capture exception details.
    """
    print("\n=== Exception Details ===")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")


def demo_finally_clause():
    """
    Demonstrates the use of a finally clause.
    The finally block executes regardless of whether an exception was raised.
    """
    print("\n=== Finally Clause ===")
    try:
        result = 10 / 5
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("This will run no matter what.")


def demo_raise_exception():
    """
    Demonstrates how to raise an exception manually.
    """
    print("\n=== Raise Exception ===")
    try:
        raise ValueError("This is a custom error message.")
    except ValueError as e:
        print(f"Caught an exception: {e}")


if __name__ == "__main__":
    demo_simple_exception()
    demo_multiple_exceptions()
    demo_exception_details()
    demo_finally_clause()
    demo_raise_exception()
