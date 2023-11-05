import os
import sys

from PyPDF2 import PdfFileMerger, PdfReader, PdfWriter

from config import (input_directory, output_directory, watermark_output_path,
                    watermark_string)
from watermark import create_watermark


def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    """Add watermark to all pages of a pdf file and generates a final pdf file

    Args:
        input_pdf_path (str): pdf file path
        output_pdf_path (str): output pdf file path
        watermark_pdf_path (str): the original pdf file where watermark is stored. Results from watermark.py
    """


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

    
