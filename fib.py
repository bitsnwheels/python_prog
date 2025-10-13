def fib(n):
    try:
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    except ValueError as e:
        # In a test scenario, you don't want to print an error and return None.
        # You want to let the exception propagate so pytest can catch it.
        # So we'll let the exception be raised.
        raise e
    except Exception as e:
        print("Some error occurred:", e)
        # You should also raise an exception here to signal the failure.
        raise

if __name__ == "__main__":
    # This code will only run when you execute fib.py directly.
    try:
        n = int(input("Enter the value of n: "))
        result = fib(n)
        if result is not None:  # Check if fib returned a value
            print(result)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)