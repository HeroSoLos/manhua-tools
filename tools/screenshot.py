import pyautogui

def get_upper_middle_region():
    """
    Get the region coordinates of the upper middle third portion of the screen.

    :return: A tuple (x, y, width, height) representing the region.
    """
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Calculate dimensions
    upper_height = screen_height // 4

    x = 0  # Start from the second third (middle)
    y = 0  # Start at the top of the screen
    width = screen_width  # Width of the middle third
    height = upper_height*3  # Height is half of the screen

    return (x, y, width, height)

# Function to take a screenshot
def take_screenshot(region=None, filename="screenshot.png"):
    # Capture the specified region of the screen
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot to a file
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")



if __name__ == "__main__":
    take_screenshot(region=get_upper_middle_region(), filename="../screenshot.png")
