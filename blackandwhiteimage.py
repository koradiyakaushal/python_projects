from PIL import Image
open_image = Image.open("google.png")
convert_to_bw = open_image.convert("L")
convert_to_bw.show()