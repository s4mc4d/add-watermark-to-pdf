from PyPDF2 import PdfReader, PdfWriter, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import os
import sys
from dotenv import load_dotenv

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


def process_all_files_sequentially(source_dir, target_dir, watermark_text):
    # Create the output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each PDF in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(input_directory, filename)
            output_pdf_path = os.path.join(output_directory, f'{filename}')
            add_watermark(input_pdf_path, output_pdf_path, watermark_output_path)
            print(f'Watermark added to {filename}')


if __name__=="__main__":
    
    # Use environment variables for the paths
    load_dotenv()
    input_directory = os.getenv('WATERMARK_INPUT_FOLDER', '/default/path/to/input/folder')
    output_directory = os.getenv('WATERMARK_OUTPUT_FOLDER', '/default/path/to/output/folder')
    watermark_output_path = os.getenv('WATERMARK_PATH', 'watermark.pdf')
    watermark_string = os.getenv('WATERMARK_TEXT', 'Confidential')


    process_all_files_sequentially(input_directory,
                                    output_directory,
                                    watermark_string)

    
