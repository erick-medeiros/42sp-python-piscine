from ft_filter import ft_filter


def main():
    """
    Main function to test ft_filter with various cases.
    """

    # Test 0: filter docstring
    assert ft_filter.__doc__ == filter.__doc__

    # Test 1: Filter even numbers
    result = list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    assert result == [2, 4], f"Expected [2, 4], got {result}"

    # Test 2: Filter non-empty strings
    result = list(ft_filter(lambda x: len(x) > 0, ["", "abc", "def", ""]))
    assert result == ["abc", "def"], f"Expected ['abc', 'def'], got {result}"

    # Test 3: No element passes
    result = list(ft_filter(lambda x: x > 10, [1, 2, 3]))
    assert result == [], f"Expected [], got {result}"

    # Test 4: Filter negative numbers
    result = list(ft_filter(lambda x: x < 0, [-2, -1, 0, 1, 2]))
    assert result == [-2, -1], f"Expected [-2, -1], got {result}"

    # Test 5: Filter with always True predicate
    result = list(ft_filter(lambda x: True, [1, 2, 3]))
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"

    # Test 6: Filter with always False predicate
    result = list(ft_filter(lambda x: False, [1, 2, 3]))
    assert result == [], f"Expected [], got {result}"

    # Test 7: Filter empty input
    result = list(ft_filter(lambda x: x > 0, []))
    assert result == [], f"Expected [], got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    main()
