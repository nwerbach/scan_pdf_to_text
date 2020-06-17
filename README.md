# scan_pdf_to_text
Extract text from an scanned pdf file

# Steps before you start
Go to https://github.com/UB-Mannheim/tesseract/wiki and download tesseract exe file

pip install pytesseract
pip install pdf2image
pip install PIL

add following part to all your tesseract python files if PATH couldnt be changed
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/nicolas.werbach/AppData/Local/Tesseract-OCR/tesseract.exe'
