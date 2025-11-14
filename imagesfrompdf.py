#isAww
import fitz
import os

def extract_images_from_pdf(pdf_path, output_dir="temp/pdfimages/"):
    """
    Extracts all images from a PDF and saves them into a directory.

    Args:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Directory where extracted images will be saved.
    """

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF
    pdf = fitz.open(pdf_path)

    img_count = 0  # Counter for naming images

    for page_num in range(len(pdf)):
        page = pdf[page_num]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]  # Reference ID of the image
            pix = pdf.extract_image(xref)

            image_bytes = pix["image"]
            image_ext = pix["ext"]

            img_count += 1

            image_filename = os.path.join(
                output_dir,
                f"page{page_num+1}_img{img_count}.{image_ext}"
            )

            # Save the image
            with open(image_filename, "wb") as f:
                f.write(image_bytes)

            print(f"Saved: {image_filename}")

    print(f"\nTotal images extracted: {img_count}")
