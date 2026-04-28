import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(arr: np.ndarray) -> np.ndarray:
    """Zoom into the center of the image, extract grayscale channel."""
    h, w = arr.shape[:2]
    cy, cx = h // 2, w // 2
    half = 200
    sliced = arr[cy - half: cy + half, cx - half: cx + half, 0:1]
    return sliced


def main():
    """Load animal.jpeg, print info, zoom and display it."""
    try:
        arr = ft_load("animal.jpeg")
        if arr is None:
            return
        print(arr)
        zoomed = zoom(arr)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        plt.imshow(zoomed[:, :, 0], cmap="gray")
        plt.title("Zoomed")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
