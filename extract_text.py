from PyPDF2 import PdfReader

def extract_text(input_file):
    reader = PdfReader(input_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text