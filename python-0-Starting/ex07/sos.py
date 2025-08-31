import sys


NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ ",
}


def main():
    """
    Main function to convert input string to Morse code.
    Accepts exactly one command-line argument: a string.
    Outputs the Morse code equivalent of the string.
    """

    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")

        text = sys.argv[1].upper()
        morse_code = ""

        for char in text:
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            morse_code += NESTED_MORSE[char]

        morse_code = morse_code.rstrip()
        print(morse_code)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
