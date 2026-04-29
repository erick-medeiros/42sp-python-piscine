import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print shape of 2D array and return a sliced version of it."""

    if not isinstance(family, list):
        raise TypeError("family must be a list")

    if not family:
        raise ValueError("family must not be empty")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")

    row_len = len(family[0])

    if not all(len(row) == row_len for row in family):
        raise ValueError("All rows must have the same size")

    arr = np.array(family)
    print(f"My shape is : {arr.shape}")

    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")

    return sliced.tolist()


def main():
    """Test slice_me function."""
    try:
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2],
        ]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
