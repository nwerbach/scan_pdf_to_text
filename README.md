# Scanned PDF to Text File
## Description
This tool converts a scanned PDF file into plain text using OCR. Advantageous are predominantly searchable text. The mose powerful use is a combination of both to work with, as the tool has some problems recognising some representations within the PDF (e.g. tables).

In general the tool converts each PDF page into a picture, which than will be analysed and it will try to recognize characters and words (depending on the language set by the user).

## Before you start
 In order to use the tool please follow these steps:
 
 - Download OCR Library (*tesseract.exe*) provided by Uni Mannheim: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
 - Install depending Python libraries
 ```Python
pip install pdf2image
pip install PIL
```
- add following part to all your *tesseract* python files in the beginning, if *PATH* couldn't be changed 
```Python
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/nicolas.werbach/AppData/Local/Tesseract-OCR/tesseract.exe'
```
