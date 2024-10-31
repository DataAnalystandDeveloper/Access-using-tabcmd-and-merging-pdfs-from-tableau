import subprocess
from glob2 import glob
from PyPDF2 import PdfMerger
import fitz  # PyMuPDF
import os

def export_view(view_url, output_pdf):
    command = [
        'tabcmd',
        'export',
        '-t', 'irgrahub',
        view_url,
        '--pdf',
        '-f', output_pdf
    ]
    subprocess.run(command, check=True)

def is_blank_page(pdf_path, intensity_threshold=240, white_ratio_threshold=0.99):
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            pix = page.get_pixmap(colorspace="gray")  # Convert to grayscale
            white_pixel_count = sum(1 for pixel in pix.samples if pixel > intensity_threshold)
            white_ratio = white_pixel_count / len(pix.samples)
            if white_ratio < white_ratio_threshold:
                return False
    return True

def pdf_merger():
    file_merger = PdfMerger()
    pdfs_stored = [filename for filename in glob(r"C:\Users\jespinoza\Desktop\Python\PDF_Outputs\*.pdf")]
    
    for pdf in pdfs_stored:
        if not is_blank_page(pdf):
            file_merger.append(pdf)

    merged_pdf_path = r"C:\Users\jespinoza\Desktop\Python\PDF_Outputs\Merged_pdfs.pdf"
    with open(merged_pdf_path, "wb") as new_file:
        file_merger.write(new_file)
    return merged_pdf_path

def add_page_numbers(pdf_path):
    temp_pdf_path = pdf_path.replace(".pdf", "_numbered.pdf")
    with fitz.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = f"Page {page_number}"
            text_position = (page.rect.width - 100, page.rect.height - 50)  # Bottom-right corner
            page.insert_text(text_position, text, fontsize=12, color=(0, 0, 0))
        pdf.save(temp_pdf_path)
    
    os.replace(temp_pdf_path, pdf_path)  # Replace original PDF with numbered PDF

def additional_function():
    print("Additional function from another script.")

def main():
    views_file_path = r"C:\Users\jespinoza\Desktop\Python\PDF_Outputs\views_file.txt"

    # Read views from the file
    with open(views_file_path, "r") as views_file:
        views_to_export = [line.strip().split(',') for line in views_file]

    # Export views
    for view in views_to_export:
        entity_id, output_pdf = view[0], view[1]
        export_view(entity_id, output_pdf)

    # Call the additional function
    additional_function()

    print("Batch process completed.")

    # Merge PDFs and add page numbers
    merged_pdf_path = pdf_merger()
    add_page_numbers(merged_pdf_path)
    print("Page numbers added to the merged PDF.")

if __name__ == "__main__":
    main()
