import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image and return its pixel data as a numpy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("Only JPG/JPEG formats are supported")

        img = Image.open(path).convert("RGB")

        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")

        return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Test ft_load function."""
    result = ft_load("landscape.jpg")
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
