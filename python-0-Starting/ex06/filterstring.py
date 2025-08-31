import sys
from ft_filter import ft_filter


def main():
    """
    Main function to handle input and output.
    Accepts exactly two command-line arguments: a string and an integer.
    Outputs a list of words from the string that are longer than the integer.
    """
    args = sys.argv[1:]
    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        s, n = args[0], args[1]
        n = int(n)

        def func(word):
            return len(word) > n

        filtered_words = [word for word in ft_filter(func, s.split())]

        print(filtered_words)

    except (ValueError, AssertionError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
