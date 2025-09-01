import time
from time import sleep
from shutil import get_terminal_size


def format_seconds(seconds: float) -> str:
    """
    Format seconds into a string in the format MM:SS.
    """
    min, sec = divmod(int(seconds), 60)
    return f"{int(min):02d}:{int(sec):02d}"


def ft_tqdm(lst: range) -> None:
    """
    A simple implementation of a progress bar similar to tqdm.
    """
    total_items = len(lst)
    start_timestamp = time.time()

    terminal_width = get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for index, element in enumerate(lst, start=1):
        progress = int(index / total_items * progress_bar_width)
        elapsed_timestamp = time.time() - start_timestamp
        speed = index / elapsed_timestamp
        remaining_time = (total_items - index) / speed

        elapsed_str = format_seconds(elapsed_timestamp)
        remaining_str = format_seconds(remaining_time)

        progress_bar = f"{'█' * progress:<{progress_bar_width}}"

        percentage = progress * 100 // progress_bar_width

        bar_info = f"{percentage}%|{progress_bar}| {index}/{total_items}"
        time_info = f"[{elapsed_str}<{remaining_str}, {speed:.2f}it/s]"

        print(f"\r{bar_info} {time_info}", end="", flush=True)
        yield element


def main():
    """
    Test the ft_tqdm function.
    """
    for ele in ft_tqdm(range(333)):
        sleep(0.005)


if __name__ == "__main__":
    main()
