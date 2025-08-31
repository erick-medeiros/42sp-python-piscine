import sys


def analyze_text(text: str) -> dict:
    """
    Analyzes the input text and counts the occurrences of
    uppercase letters, lowercase letters, digits, punctuation,
    and spaces.
    """

    # string.punctuation
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    counts = {
        "upper": 0,
        "lower": 0,
        "digits": 0,
        "punctuation": 0,
        "spaces": 0,
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char in punctuation_chars:
            counts["punctuation"] += 1
        elif char.isspace():
            counts["spaces"] += 1
    return counts


def main():
    """
    Main function to handle input and output.
    Accepts a single command-line argument or prompts the user for input.
    Outputs the analysis of the text.
    """
    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if len(args) == 0:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = args[0]

        counts = analyze_text(text)
        total = len(text)
        print(f"The text contains {total} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
