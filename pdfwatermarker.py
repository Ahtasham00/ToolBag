import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def add_watermark_to_pdf(input_pdf_path, watermark_text):
    # Create watermark PDF in memory
    watermark_stream = BytesIO()
    c = canvas.Canvas(watermark_stream, pagesize=letter)
    c.setFont("Helvetica", 40)
    c.setFillColorRGB(0.6, 0.6, 0.6, alpha=0.3)
    c.saveState()
    c.translate(300, 400)
    c.rotate(45)
    c.drawCentredString(0, 0, watermark_text)
    c.restoreState()
    c.save()
    watermark_stream.seek(0)

    # Read watermark and input PDF
    watermark_pdf = PdfReader(watermark_stream)
    watermark_page = watermark_pdf.pages[0]
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Apply watermark to each page
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    # Prepare output path
    os.makedirs("temp", exist_ok=True)
    output_path = os.path.join("temp", f"watermarked_{os.path.basename(input_pdf_path)}")
    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path