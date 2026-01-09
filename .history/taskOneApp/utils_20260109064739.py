from pdf2image import convert_from_path
from PIL import Image
import os

POPPLER_PATH = r"C:\poppler\poppler-25.12.0\Library\bin"

def convert_file(input_path, from_ext, to_ext, output_path):
    from_ext = from_ext.lower()
    to_ext = to_ext.lower()

    if from_ext == to_ext:
        raise ValueError("From and To formats cannot be same")

    # PDF → IMAGE
    if from_ext == 'pdf' and to_ext in ['jpg', 'png']:
        images = convert_from_path(
            input_path,
            dpi=200,
            poppler_path=POPPLER_PATH
        )
        images[0].save(output_path, to_ext.upper())
        return

    # IMAGE → IMAGE
    if from_ext in ['jpg', 'png'] and to_ext in ['jpg', 'png']:
        img = Image.open(input_path)
        img.convert("RGB").save(output_path, to_ext.upper())
        return

    # IMAGE → PDF
    if from_ext in ['jpg', 'png'] and to_ext == 'pdf':
        img = Image.open(input_path)
        img.convert("RGB").save(output_path, "PDF")
        return

    raise ValueError("Conversion not supported")
