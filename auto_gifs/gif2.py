
from PIL import Image
import os

path, dirs, files = next(os.walk("frames"))
file_count = len(files)
image_var=[]

frames = []

width = 500
height = 500
count =0
temp_image = Image.new("1", (width, height), (255))



for x in range(file_count/3):

	
	image_file = ("frames/"+str (count+1)+'.png')


	new_frame = Image.open(image_file)
	imResize = new_frame.resize((400,400), Image.BICUBIC)
	imResize2 = imResize.resize((500,500), Image.ANTIALIAS)
	imResize2.quantize(colors=256)
	imResize2 = imResize2.convert('P', palette=imResize2.getpalette(), colors=16)
	frames.append(imResize2)
	count = count + 3
	
	


#im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=100, loop=0)
frames[0].save("fade.gif", save_all=True, append_images=frames[1:], duration=150, loop=0,optimize=True)

print(file_count)