#isAww
from PIL import Image
from rembg import remove
input_path="temp/input_image.png"
output_path="temp/output_image.jpg"
def remove_background(input_path,output_path):
    inp=Image.open(input_path)
    output=remove(inp)
    output.save(output_path)

remove_background(input_path,output_path)

