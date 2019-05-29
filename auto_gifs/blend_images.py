from PIL import Image


def blend_mid():
	

	background = Image.open("frames/8.png")
	overlay = Image.open("frames/10.png")
	background = background.convert("RGB")
	overlay = overlay.convert("RGB")
	new_img = Image.blend(background, overlay, 0.5)
	new_img.save("frames/9.png","PNG")

def blend_ends():
	

	background = Image.open("frames/0.png")
	overlay = Image.open("frames/18.png")
	background = background.convert("RGB")
	overlay = overlay.convert("RGB")
	new_img = Image.blend(background, overlay, 0.5)
	new_img.save("frames/19.png","PNG")




