from pdf2image import convert_from_path
from PIL import Image

def convert_file(input_path, from_ext, to_ext, output_path):
    if from_ext == to_ext:
        raise ValueError("From and To formats cannot be same")

    if from_ext == 'pdf' and to_ext in ['jpg', 'png']:
        images = convert_from_path(input_path)
        images[0].save(output_path)
        return

    if from_ext in ['jpg', 'png'] and to_ext in ['jpg', 'png']:
        img = Image.open(input_path)
        img.convert('RGB').save(output_path)
        return

    if from_ext in ['jpg', 'png'] and to_ext == 'pdf':
        img = Image.open(input_path)
        img.convert('RGB').save(output_path)
        return

    raise ValueError("Conversion not supported")