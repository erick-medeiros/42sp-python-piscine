"""Module with color filter functions for images."""
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the colors of the image received.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with inverted colors.
    """
    result = 255 - array
    plt.imshow(result)
    plt.show()
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    """Apply a red filter to the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the red channel.
    """
    result = array * [1, 0, 0]
    plt.imshow(result)
    plt.show()
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Apply a green filter to the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the green channel.
    """
    result = array - array * [1, 0, 1]
    plt.imshow(result)
    plt.show()
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Apply a blue filter to the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array with only the blue channel.
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    plt.imshow(result)
    plt.show()
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Apply a grey filter to the image.

    Args:
        array: numpy array of the image in RGB format.

    Returns:
        numpy array in greyscale.
    """
    result = array / [3, 3, 3]
    result = (result[:, :, 0] + result[:, :, 1] + result[:, :, 2])
    result = np.stack([result, result, result], axis=2).astype(np.uint8)
    plt.imshow(result, cmap='gray')
    plt.show()
    return result


def main():
    """Test all filter functions."""
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
