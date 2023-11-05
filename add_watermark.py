import os
import sys

from PyPDF2 import PdfFileMerger, PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from config import (input_directory, output_directory, watermark_output_path,
                    watermark_string)


def create_watermark(content, output_path):
    # Create a PDF file with ReportLab
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    # Define positions for the watermark
    # These positions are set to distribute the watermark evenly across the page
    positions = [
        (width * 0.25, height * 0.75), 
        (width * 0.75, height * 0.75),
        (width * 0.25, height * 0.25),
        (width * 0.75, height * 0.25),
    ]
    for pos in positions:
        c.saveState()
        c.translate(pos[0], pos[1])
        c.rotate(30)
        c.setFillColorRGB(0, 0, 0, 0.3)  # Set the transparency of the watermark
        c.setFont("Helvetica", 30)
        # Draw the text string centered at the position
        c.drawCentredString(0, 0, content)
        c.restoreState()
    c.save()


def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    # Create a PdfFileReader object for the original PDF
    input_pdf = PdfReader(input_pdf_path)
    # Create a PdfFileReader object for the watermark PDF
    watermark_pdf = PdfReader(watermark_pdf_path)
    watermark_page = watermark_pdf.pages[0]

    # Create a PdfFileWriter object for the output PDF
    pdf_writer = PdfWriter()

    # Apply the watermark to each page
    for page_number in range(len(input_pdf.pages)):
        page = input_pdf.pages[page_number]
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    # Write the watermarked PDF to the output file
    with open(output_pdf_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)


def process_all_files_sequentially(source_dir, target_dir, watermark_path):
    # Create the output directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Process each PDF in the input directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(source_dir, filename)
            output_pdf_path = os.path.join(target_dir, f'{filename}')
            add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path=watermark_path)
            print(f'Watermark added to {filename}')


if __name__=="__main__":
    
    # Creation of watermark
    create_watermark(watermark_string,watermark_output_path)
    
    # launching sequence to process all pdf
    process_all_files_sequentially(input_directory,
                                    output_directory,
                                    watermark_output_path)

    
