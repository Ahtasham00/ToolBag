#isAww
import os
from PIL import Image

def convert_to_png(input_path):
    # Ensure temp directory exists
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    # Extract filename without extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(temp_dir, f"{base_name}.png")

    # Open and convert image
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGBA")  # Preserve transparency if present
            img.save(output_path, "PNG")
        return output_path
    except Exception as e:
        raise RuntimeError(f"Failed to convert image: {e}")