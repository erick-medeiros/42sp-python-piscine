"""Module to load, slice, transpose and display an image."""
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D array manually without using any library.

    Args:
        array: numpy array of shape (rows, cols).

    Returns:
        Transposed numpy array of shape (cols, rows).
    """
    rows, cols = array.shape
    result = np.empty((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = array[i][j]
    return result


def zoom_image(array: np.ndarray) -> np.ndarray:
    """Slice a 400x400 square and convert to grayscale (1 channel).

    Args:
        array: numpy array of the original image in RGB format.

    Returns:
        numpy array of shape (400, 400, 1) in grayscale.
    """
    sliced = array[0:400, 0:400]
    grey = np.mean(sliced, axis=2, keepdims=True).astype(np.uint8)
    return grey


def display_image(array: np.ndarray) -> None:
    """Display the image with axis scales.

    Args:
        array: 2D numpy array to display.
    """
    plt.figure()
    plt.imshow(array, cmap='gray')
    plt.show()


def main():
    """Load animal.jpeg, slice, transpose manually, and display."""
    try:
        array = ft_load("animal.jpeg")
        if array is None:
            return

        grey = zoom_image(array)
        print(f"The shape of image is: {grey.shape} or {grey[:, :, 0].shape}")
        print(grey)

        grey_2d = grey[:, :, 0]
        transposed = manual_transpose(grey_2d)

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        display_image(transposed)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
