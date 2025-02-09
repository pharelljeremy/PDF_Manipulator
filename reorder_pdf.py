# reorder_pdf.py
from PyPDF2 import PdfReader, PdfWriter

def reorder_pdf(input_file, page_order, output_file):
    """
    Reorder pages in a PDF file according to the specified order.
    
    Args:
        input_file (str): Path to input PDF file
        page_order (list): List of page numbers in desired order (1-based indexing)
        output_file (str): Path to save the reordered PDF
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()
    
    # Validate page numbers
    max_pages = len(reader.pages)
    for page_num in page_order:
        if page_num < 1 or page_num > max_pages:
            raise ValueError(f"Invalid page number {page_num}. PDF has {max_pages} pages.")
    
    # Add pages in specified order
    for page_num in page_order:
        writer.add_page(reader.pages[page_num - 1])  # Convert to 0-based index
    
    # Save the reordered PDF
    with open(output_file, 'wb') as output_pdf:
        writer.write(output_pdf)