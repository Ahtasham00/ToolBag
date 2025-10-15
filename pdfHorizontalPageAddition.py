#isAww
from pypdf import PdfReader, PdfWriter, PageObject

input_path = "file1.pdf"
output_path = "outputfile1.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Loop through pages two at a time
for i in range(0, len(reader.pages), 2):
    # Get the first page
    page1 = reader.pages[i]
    width, height = page1.mediabox.width, page1.mediabox.height

    # Create a blank page double the width
    new_page = PageObject.create_blank_page(width=width * 2, height=height)
    new_page.merge_page(page1)

    # If there’s a second page, merge it beside the first
    if i + 1 < len(reader.pages):
        page2 = reader.pages[i + 1]
        new_page.merge_translated_page(page2, tx=width, ty=0)

    writer.add_page(new_page)

# Save new PDF
with open(output_path, "wb") as f:
    writer.write(f)

print("✅ PDF created:", output_path)
