from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_file, watermark_file, output_file):
    reader = PdfReader(input_file)
    watermark = PdfReader(watermark_file)
    writer = PdfWriter()

    watermark_page = watermark.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_file, 'wb') as output_pdf:
        writer.write(output_pdf)