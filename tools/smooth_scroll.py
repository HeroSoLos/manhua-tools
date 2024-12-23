import pyautogui
import time


def smooth_scroll(amount, step=10, delay=0.01):
    """
    Smoothly scroll by dividing the scroll action into smaller steps.
    :param amount: Total scroll amount (positive for upward, negative for downward).
    :param step: Incremental scroll amount for each step.
    :param delay: Delay between each step in seconds.
    """
    direction = 1 if amount > 0 else -1
    steps = abs(amount) // step
    remainder = abs(amount) % step

    # Perform scrolling in smooth steps
    for _ in range(steps):
        pyautogui.scroll(direction * step)
        time.sleep(delay)

    # Scroll remaining amount if there is any
    if remainder != 0:
        pyautogui.scroll(direction * remainder)


if __name__ == "__main__":
    smooth_scroll(-200, step=10, delay=0.02)
