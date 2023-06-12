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
    tables = tabula.read_pdf(file_path, multiple_tables=True, guess=True, stream=True, pages="all")

    print(tables)
    
    return tables


# PDF filepaths
path = '/Users/talhaehtasham/Desktop/MedThread Demo/MedThreadDemo/Papers/'
parsed_path = '/Users/talhaehtasham/Desktop/MedThread Demo/MedThreadDemo/ParsedPapers/'
paper_title = 'Association of Powder Use in the Genital Area With Risk of Ovarian Cancer - PMC.pdf'
file_path = path + paper_title

# Extract text 
pdf_text = pdf_to_text(file_path)

# Write text output to file
text_file = parsed_path + paper_title + " (TEXT).txt"
with open(text_file, 'w') as f:
    f.write(pdf_text)

# Extract tables
pdf_tables = pdf_to_tables(file_path)

# Write tables to CSV
csv_file = parsed_path + paper_title + " (TABLES).csv"
pdf_tables[0].to_csv(csv_file)
