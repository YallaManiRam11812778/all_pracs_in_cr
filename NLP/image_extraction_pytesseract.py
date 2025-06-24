from PIL import Image
from pytesseract import pytesseract
import enum

class ImageReader:
    def extract_text(self, image: str, lang="eng") -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text
    
if __name__ == "__main__":
    ir = ImageReader()
    text = ir.extract_text("/home/caratred/Downloads/pos_checks_images/pos_checks_images/cropped/pos-@2024-03-07@20240322103849049dwt.png")
    print(text)