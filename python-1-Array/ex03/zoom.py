"""Module to load, zoom and display an image as grayscale."""
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(array: np.ndarray) -> np.ndarray:
    """Slice a 400x400 square and convert it to grayscale.

    Args:
        array: numpy array of the original image in RGB format.

    Returns:
        numpy array of shape (400, 400, 1) in grayscale, or None on error.
    """
    try:
        sliced = array[0:400, 0:400]
        grey = np.mean(sliced, axis=2, keepdims=True).astype(np.uint8)
        return grey
    except Exception as e:
        print(f"Error: {e}")
        return None


def display_image(grey: np.ndarray) -> None:
    """Display a grayscale image with labelled axis scales.

    Args:
        grey: numpy array of shape (400, 400, 1).
    """
    try:
        plt.figure()
        plt.imshow(grey[:, :, 0], cmap='gray')
        plt.xlabel("X scale (pixels)")
        plt.ylabel("Y scale (pixels)")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Load animal.jpeg, zoom in, and display the grayscale result."""
    try:
        array = ft_load("animal.jpeg")
        if array is None:
            return

        print(array)
        grey = zoom_image(array)
        print(f"New shape after slicing: {grey.shape}")
        print(grey)

        display_image(grey)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
