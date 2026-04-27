def slice_me(family: list, start: int, end: int) -> list:
    # your code here
    pass


def main():
    """Test slice_me function."""
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
