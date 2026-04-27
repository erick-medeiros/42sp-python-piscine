import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate BMI from height (m) and weight (kg) lists."""

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Arguments must be lists")

    if len(height) != len(weight):
        raise ValueError("Lists must be the same size")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("List elements must be int or float")

    h = np.array(height, dtype=float)
    w = np.array(weight, dtype=float)

    return [float(v) for v in w / (h**2)]


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """Return a list of booleans, True if bmi value is above limit."""

    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if not all(isinstance(i, (int, float)) for i in bmi):
        raise TypeError("List elements must be int or float")

    if not isinstance(limit, int):
        raise TypeError("limit must be an int")

    arr = np.array(bmi)

    return [bool(v) for v in arr > limit]


def main():
    """Test give_bmi and apply_limit functions."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
