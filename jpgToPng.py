#isAww
import os
import tempfile
from PIL import Image

def convert_jpg_to_png(jpg_path: str) -> str:
    """
    Converts a JPG image to PNG and stores it in a temporary directory.
    
    Args:
        jpg_path (str): Path to the input JPG file.
        
    Returns:
        str: Path to the converted PNG file in the temp directory.
    """
    # Ensure the file exists
    if not os.path.isfile(jpg_path):
        raise FileNotFoundError(f"File not found: {jpg_path}")
    
    # Open the JPG image
    with Image.open(jpg_path) as img:
        # Create a temp directory
        temp_dir = tempfile.gettempdir()
        # Create a PNG file name
        base_name = os.path.splitext(os.path.basename(jpg_path))[0]
        png_path = os.path.join(temp_dir, f"{base_name}.png")
        # Save the image as PNG
        img.save(png_path, "PNG")
    
    return png_path

# Example usage
# png_file = convert_jpg_to_png("example.jpg")
# print("Converted PNG saved at:", png_file)
