from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_file, output_file, angle=90):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    
    with open(output_file, 'wb') as output_pdf:
        writer.write(output_pdf)