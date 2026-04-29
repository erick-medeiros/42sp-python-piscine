"""Module to compute BMI values and flag entries above a limit."""
import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Compute the BMI for each (height, weight) pair.

    Args:
        height: list of heights in meters (int or float).
        weight: list of weights in kilograms (int or float).

    Returns:
        List of BMI values as floats, or None on error.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Arguments must be lists")

        if len(height) != len(weight):
            raise ValueError("Lists must be the same size")

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise TypeError("List elements must be int or float")

        h = np.array(height, dtype=float)
        w = np.array(weight, dtype=float)

        return [float(v) for v in w / (h**2)]
    except Exception as e:
        print(f"Error: {e}")
        return None


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """Return a list of booleans flagging BMI values above a limit.

    Args:
        bmi: list of BMI values (int or float).
        limit: integer threshold.

    Returns:
        List of booleans (True where bmi > limit), or None on error.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")

        if not all(isinstance(i, (int, float)) for i in bmi):
            raise TypeError("List elements must be int or float")

        if not isinstance(limit, int):
            raise TypeError("limit must be an int")

        arr = np.array(bmi)

        return [bool(v) for v in arr > limit]
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Run a quick test of give_bmi and apply_limit."""
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
