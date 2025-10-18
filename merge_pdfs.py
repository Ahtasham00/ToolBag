#isAww
import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf1_path, pdf2_path):
    # Ensure temp directory exists
    os.makedirs("temp", exist_ok=True)
    
    # Define merged file path
    merged_path = os.path.join("temp", "merged.pdf")
    
    # Merge the PDFs
    merger = PdfMerger()
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    merger.write(merged_path)
    merger.close()
    
    return merged_path
