from PIL import Image
import pytesseract
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core(r"C:\Users\user\Downloads\WhatsApp Image 2020-09-14 at 10.23.38.jpeg"))
