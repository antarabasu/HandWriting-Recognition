# STEP:2. This step is optional if the background of the image is not white
# the algorith that I have used will not yield 100% result with dark background. This code is to make transparent background

# if the background looks bit dusky, then get a white background
from PIL import Image

def convertToPNG():
    image= Image.open('../HandWriting-Recognition/new_data/test/test_sharpen.png')
    background = Image.new('RGBA', image.size, (255, 255, 255))
    img = image.convert('RGBA')
    background.paste(img, img)
    background.save('../HandWriting-Recognition/new_data/test/test_sharpen_new.png', "PNG")
    print('Done')

convertToPNG()