import sys

try:
    args = sys.argv[1:]

    if len(args) == 0:
        exit()
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")

    n = int(args[0])

    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
