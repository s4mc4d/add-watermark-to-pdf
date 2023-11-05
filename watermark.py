from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import argparse
import os

def create_watermark(content, output_path):
    """Generates  a watermark with 'content' string and creates a pdf to output_path

    Args:
        content (str): content of the watermark
        output_path (str): path of watermark pdf file
    """

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

    return True


if __name__=="__main__":

    parser = argparse.ArgumentParser(description="Generates a watermark as a pdf file from a string")
    parser.add_argument("-p","--output_path", help="The full output path to the watermark PDF file.",required=True)
    parser.add_argument("-t","--watermark_text", help="The text to be used as a watermark.", default="Confidential")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Use the arguments to define the paths
    output_path = args.output_path
    watermark_string = args.watermark_text
    
    create_watermark(watermark_string, output_path)


