from tools.screenshot import  *
from tools.text_recognition import text_recognition
from tools.smooth_scroll import smooth_scroll
import time
import keyboard
import winsound
import pyautogui

time.sleep(3)

pause = False
while True:
    smooth_scroll(-1000, 200, 0.01)
    image_name = "screenshot.png"

    if keyboard.is_pressed('x'):
        pause = True

    take_screenshot(get_upper_middle_region(), image_name)
    extracted_text = text_recognition(image_name)
    extracted_list = extracted_text.replace("\n", " ").split(" ")
    extracted_list = [word.translate(str.maketrans('', '', ".,!?;:'\"-()")) for word in extracted_list
                      if len(word.translate(str.maketrans('', '', ".,!?;:'\"-()"))) > 3]
    length_extracted_list = len(extracted_list)

    if keyboard.is_pressed('x'):
        pause = True

    print(extracted_list)
    print(length_extracted_list)
    
    if "comment" in extracted_list or "Comments" in extracted_list or "Comment" in extracted_list or "comments" in extracted_list or "chapter" in extracted_list or "Chapter" in extracted_list:
        print("next page")
        keyboard.press_and_release('right')
        time.sleep(3)
        pyautogui.scroll(-1000)
        time.sleep(2)
    else:

    
    # if length_extracted_list//3 > 3:
    #     winsound.Beep(450, 200)
    #     if keyboard.is_pressed("x"):
    #         pause = True

    #     pyautogui.scroll(-1000)
    #     time.sleep(1)
    # else:
    #     pass
    #
    # if pause:
    #     winsound.Beep(1000, 200)
    while pause:
        print("paused")
        time.sleep(0.5)
        if keyboard.is_pressed("x"):
            pause = False
            break