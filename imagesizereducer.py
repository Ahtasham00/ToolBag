#isAww
from PIL import Image
import os

def reduce_image_size(input_path, output_path, target_size_kb=1024):
    """
    Reduce image size to under target_size_kb (default 1024 KB = 1 MB).
    Supports PNG and JPG formats.
    """
    img = Image.open(input_path)
    format = img.format

    # Convert PNG to RGB if needed
    if format == 'PNG' and img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
        format = 'JPEG'  # Save as JPEG to allow compression

    quality = 95
    step = 5

    while True:
        img.save(output_path, format=format, quality=quality)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= target_size_kb or quality <= 10:
            break
        quality -= step

    print(f"Final size: {size_kb:.2f} KB at quality {quality}")

# Example usage
reduce_image_size("Profile Picture.png", "Profile Picture 1.jpg")