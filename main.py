from merge_pdfs import merge_pdfs
from split_pdfs import split_pdf
from extract_text import extract_text
from rotate_pdfs import rotate_pdf
from add_watermark import add_watermark
from pdf_utils import get_file_list, get_output_file
from reorder_pdf import reorder_pdf

def main():
    print("PDF Manipulator")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Extract Text")
    print("4. Rotate PDF")
    print("5. Add Watermark")
    print("6. Reorder Pages")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        files = get_file_list("Enter PDF files to merge (comma-separated): ")
        output = get_output_file("Enter output file name: ")
        merge_pdfs(files, output)
    elif choice == 2:
        input_file = input("Enter input file: ").strip()
        start = int(input("Enter start page: "))
        end = int(input("Enter end page: "))
        output = get_output_file("Enter output file name: ")
        split_pdf(input_file, start, end, output)
    elif choice == 3:
        input_file = input("Enter input file: ").strip()
        text = extract_text(input_file)
        print("Extracted Text:\n", text)
    elif choice == 4:
        input_file = input("Enter input file: ").strip()
        angle = int(input("Enter rotation angle (e.g., 90, 180): "))
        output = get_output_file("Enter output file name: ")
        rotate_pdf(input_file, output, angle)
    elif choice == 5:
        input_file = input("Enter input file: ").strip()
        watermark_file = input("Enter watermark file: ").strip()
        output = get_output_file("Enter output file name: ")
        add_watermark(input_file, watermark_file, output)
    elif choice == 6:
        try:
            input_file = input("Enter input file: ").strip()
            page_order = input("Enter page order (comma-separated, e.g., 3,1,2): ").strip()
            page_order = [int(x) for x in page_order.split(',')]
            output = get_output_file("Enter output file name: ")
            if not output.endswith('.pdf'):
                output += '.pdf'
            reorder_pdf(input_file, page_order, output)
            print(f"Success! Reordered PDF saved to {output}")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()