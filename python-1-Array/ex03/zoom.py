import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(array: np.ndarray) -> np.ndarray:
    """Slice a 400x400 square from the image and convert to grayscale.

    Args:
        array: numpy array of the original image in RGB format.

    Returns:
        numpy array of the zoomed grayscale image with shape (400, 400, 1).
    """
    sliced = array[0:400, 0:400]
    grey = np.mean(sliced, axis=2, keepdims=True).astype(np.uint8)
    return grey


def display_image(grey: np.ndarray) -> None:
    """Display the zoomed grayscale image with axis scales.

    Args:
        grey: numpy array of the grayscale image with shape (400, 400, 1).
    """
    plt.figure()
    plt.imshow(grey[:, :, 0], cmap='gray')
    plt.xlabel("X scale (pixels)")
    plt.ylabel("Y scale (pixels)")
    plt.show()


def main():
    """Load animal.jpeg, zoom in, print info, and display the result."""
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
