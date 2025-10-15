#isAww
#Adding page vertically
from pypdf import PdfReader, PdfWriter, PageObject

input_path = "file1.pdf"
output_path = "outputfile1.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Process pages two at a time
for i in range(0, len(reader.pages), 2):
    page1 = reader.pages[i]
    width, height = page1.mediabox.width, page1.mediabox.height

    # Create a blank page with double height
    new_page = PageObject.create_blank_page(width=width, height=height * 2)

    # Place the first page at the top
    new_page.merge_translated_page(page1, tx=0, ty=height)

    # If there’s a next page, place it below
    if i + 1 < len(reader.pages):
        page2 = reader.pages[i + 1]
        new_page.merge_page(page2)  # bottom position

    writer.add_page(new_page)

# Save the new PDF
with open(output_path, "wb") as f:
    writer.write(f)

print("✅ PDF created:", output_path)
