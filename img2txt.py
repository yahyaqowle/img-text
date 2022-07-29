import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('lvl0.png')
text = tess.image_to_string(img)

print(text)