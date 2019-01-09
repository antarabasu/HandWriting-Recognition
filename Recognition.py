# STEP:3
# This is the final step for recognizing hand written text using tesseract
# Python-tesseract is an optical character recognition (OCR) tool for python. 
# That is, it will recognize and “read” the text embedded in images.

from PIL import Image
import os.path
from pytesseract  import image_to_string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '../Tesseract-OCR/tesseract'

# identify with different .png files
Input1 = Image.open('../HandWriting-Recognition/new_data/test/test.png', mode='r')
print('Input1:',image_to_string(Input1))

Input2 = Image.open('../HandWriting-Recognition/new_data/test/littlehw.png', mode='r')
print('Input2:',image_to_string(Input2))

Input3 = Image.open('../HandWriting-Recognition/new_data/test/Text.png', mode='r')
print('Input3:',image_to_string(Input3))

# identify with different .jpeg files
Input4 = Image.open('../HandWriting-Recognition/new_data/test/4.jpeg', mode='r')
print('Input4:',image_to_string(Input4))

# identify with different .jpg files
Input5 = Image.open('../HandWriting-Recognition/new_data/test/7.jpg', mode='r')
print('Input5:',image_to_string(Input5))
