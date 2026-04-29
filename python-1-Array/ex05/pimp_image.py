"""Module with color filter functions for images."""
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the colors of the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with inverted colors, same shape as input,
        or None on error.
    """
    try:
        result = 255 - array
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the red channel, same shape as input,
        or None on error.
    """
    try:
        result = array * [1, 0, 0]
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the green channel, same shape as input,
        or None on error.
    """
    try:
        result = array.copy()
        result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
        result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the blue channel, same shape as input,
        or None on error.
    """
    try:
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the image to greyscale.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array in greyscale, same shape as input, or None on error.
    """
    try:
        result = array / 1
        grey = np.mean(result, axis=2, keepdims=True)
        result = np.repeat(grey, 3, axis=2).astype(np.uint8)
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Apply each color filter to landscape.jpg and display the results."""
    try:
        from load_image import ft_load
        array = ft_load("landscape.jpg")
        if array is None:
            return
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
