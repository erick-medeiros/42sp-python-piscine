import subprocess


def test(input, expected):
    """
    Test the Morse code conversion script with given input and expected output.
    """
    try:
        result = subprocess.run(
            ["python", "sos.py", input], capture_output=True, text=True
        )
        output = result.stdout.strip()
        assert output.strip() == expected.strip()
        print(f"Test passed for input: {input}")
    except Exception as e:
        print(f"Test failed for input: {input}. Error: {e}")
        print(f"Expected: {expected}, Got: {output}")


def main():
    """
    Test cases for the Morse code conversion script.
    """
    test_cases = [
        ("sos", "... --- ..."),
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("Python 3.8", "AssertionError: the arguments are bad"),
        ("", ""),
        ("Invalid@", "AssertionError: the arguments are bad"),
        ("123", ".---- ..--- ...--"),
    ]
    for input, expected in test_cases:
        test(input, expected)
    print("All tests finished!")


if __name__ == "__main__":
    main()
