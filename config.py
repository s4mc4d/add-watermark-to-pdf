from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration variables
input_directory = os.getenv('WATERMARK_INPUT_FOLDER', '/default/path/to/input/folder')
output_directory = os.getenv('WATERMARK_OUTPUT_FOLDER', '/default/path/to/output/folder')
watermark_output_path = os.getenv('WATERMARK_PATH', '/default/path/to/output/watermark.pdf')
watermark_string = os.getenv('WATERMARK_TEXT', 'Confidential')