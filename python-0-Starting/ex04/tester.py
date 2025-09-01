import subprocess


def test(input: list, expected):
    """
    Test function to check if the output of whatis.py.
    """
    try:
        result = subprocess.run(
            ["python", "whatis.py", *input], capture_output=True, text=True
        )
        output = result.stdout.strip()
        assert output.strip() == expected.strip()
        print(f"Test passed for input: {input}")
    except Exception as e:
        print(f"Test failed for input: {input}. Error: {e}")
        print(f"Expected: {expected}, Got: {output}")


def main():
    """
    Main function to run tests for whather a number is even or odd.
    """
    test_cases = [
        (["14"], "I'm Even."),
        (["-5"], "I'm Odd."),
        ([], ""),
        (["0"], "I'm Even."),
        (["Hi!"], "AssertionError: argument is not an integer"),
        (["13", "5"], "AssertionError: more than one argument is provided"),
    ]
    for input, expected in test_cases:
        test(input, expected)
    print("All tests finished!")


if __name__ == "__main__":
    main()
