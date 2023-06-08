from pdf2image import convert_from_path
import pytesseract
import tabula

def pdf_to_text(file_path):
    # Convert PDF to list of images
    images = convert_from_path(file_path)

    # Perform OCR on each image and concatenate the results
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)

    return text

def pdf_to_tables(file_path):
    # Extract tables fro PDF file
    tables = tabula.read_pdf(file_path, multiple_tables=True, guess=False, stream=True, pages='all')

    print(tables)
    
    return tables


# PDF filepath
path = '/Users/talhaehtasham/Desktop/MedThread Demo/MedThreadDemo/Papers/'
paper_title = 'Perineal talc exposure and epithelial ovarian cancer risk in the Central Valley of California.pdf'


# Extract text and tables
file_path = path + paper_title
#pdf_text = pdf_to_text(file_path)
pdf_tables = pdf_to_tables(file_path)


# Write text output to file
#text_file = paper_title + " (TEXT).txt"
#with open('ParsedPapers/' + text_file, 'w') as f:
#    f.write(pdf_text)

# Write table output to file
#table_file = paper_title + " (TABLES).txt"
#with open('ParsedPapers/' + table_file, 'w') as f:
#    f.write(pdf_tables)

