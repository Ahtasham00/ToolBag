#isAww
from pdf2docx import Converter

# Input and output file paths
pdf_file = "FaizanCv.pdf"        # your PDF file name
docx_file = "FaizanCv.docx"  # output Word file name

# Create converter object
cv = Converter(pdf_file)

# Convert all pages (start=0 means first page, end=None means till last)
cv.convert(docx_file, start=0, end=None)

# Close the converter
cv.close()

print("✅ PDF converted successfully with layout preserved!")
