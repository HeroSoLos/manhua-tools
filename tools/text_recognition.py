import pytesseract
from PIL import Image
import cv2
import numpy as np
import os

tesseract_path = r"tesseract/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def text_recognition(image_path):
    """
    Recognize text from an image and check if a specific word is present.
    :param image_path: Path to the image file.
    :return: Extracted text and whether the word is found.
    """
    # Read the image
    image = cv2.imread(image_path)

    # Preprocess the image: Grayscale and Thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Convert the preprocessed image to a PIL Image
    pil_image = Image.fromarray(thresh)

    # Extract text from the image
    extracted_text = pytesseract.image_to_string(pil_image, config='--psm 11')

    return extracted_text


if __name__ == "__main__":
    # Specify the path to your image
    path = "../screenshot.png"  # Replace with the actual path

    # Recognize text and check for the word "next"
    text = text_recognition(path)

    # Output results
    print("Extracted Text:")
    print(text)
