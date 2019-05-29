
from PIL import Image




def frames2gifs():
	

	background = Image.open("frames/0.png")
	overlay = Image.open("frames/19.png")
	background = background.convert("RGB")
	overlay = overlay.convert("RGB")
	new_img = Image.blend(background, overlay, 0.5)
	new_img.save("new.png","PNG")




frames2gifs()


