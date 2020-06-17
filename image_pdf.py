from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/nicolas.werbach/AppData/Local/Tesseract-OCR/tesseract.exe'

# define path to pdf file here
pdf_file = "H:/Sandbox/flag.pdf"

# *** PART 1: Converting PDF to images ***
# Store all the pages of the PDF in a variable
pages = convert_from_path(pdf_file, 500)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:
    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    filename = "page_" + str(image_counter) + ".jpg"

    # Save the image of the page in system
    page.save(filename, 'JPEG')

    # Increment the counter to update filename
    image_counter = image_counter + 1

# *** PART 2: Recognizing text from the image using OCR

# Variable to get count of total number of pages
filelimit = image_counter - 1

# Creating a text file to write the output
outfile = "flag_out.txt"

# Open the file in append mode so that
# all contents of all images are added to the same file
f = open(outfile, "wb")

# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
    # Set filename to recognize text from
    filename = "page_" + str(i) + ".jpg"

    # Recognize the text as string in image using pytesserect
    text = str(((pytesseract.image_to_string(Image.open(filename), lang="deu"))))
    # combine languages e.g. "eng+deu"
    # alternative functions:
    # image_to_boxes
    # image_to_data

    # In many PDFs at line ending a 'hyphen' is added to remove this:
    text = text.replace('-\n', '')
    #data = data.replace('-\t', '')

    # Finally write the processed text to file
    f.write(text.encode("utf-8"))

# Close the file after writing all the text
f.close()