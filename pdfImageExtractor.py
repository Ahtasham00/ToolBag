#isAww
import os
import fitz  # PyMuPDF
from PIL import Image
from zipfile import ZipFile

def extract_images_to_zip(pdf_path):
    # Setup temp directory
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    # Open PDF
    doc = fitz.open(pdf_path)
    image_paths = []

    for page_index in range(len(doc)):
        for img_index, img in enumerate(doc.get_page_images(page_index)):
            xref = img[0]
            base_name = f"page{page_index+1}_img{img_index+1}.png"
            image_path = os.path.join(temp_dir, base_name)

            # Extract and save image
            pix = fitz.Pixmap(doc, xref)
            if pix.n > 4:  # CMYK
                pix = fitz.Pixmap(fitz.csRGB, pix)
            pix.save(image_path)
            image_paths.append(image_path)

    # Create ZIP file
    zip_path = os.path.join(temp_dir, "extracted_images.zip")
    with ZipFile(zip_path, "w") as zipf:
        for img_path in image_paths:
            zipf.write(img_path, os.path.basename(img_path))

    return zip_path