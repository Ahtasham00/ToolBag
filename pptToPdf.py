import comtypes.client
import os

def ppt_to_pdf(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1
    presentation = powerpoint.Presentations.Open(input_path)
    presentation.SaveAs(output_path, 32)  # 32 = PDF format
    presentation.Close()
    powerpoint.Quit()
    print(f"✅ PDF created successfully: {output_path}")

# Example usage

input_path = "file1.pptx"
output_path = "outputfile1.pdf"

ppt_to_pdf(input_path, output_path)

#ppt_to_pdf(r"C:\Users\Ahtasham\Desktop\Note_Reducer\Lecture 2.pptx", 
#           r"C:\Users\Ahtasham\Desktop\Note_Reducer\output.pdf")
