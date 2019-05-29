from PIL import Image
import random
import os

def frames2gifs():
	path, dirs, files = next(os.walk("frames"))
	file_count = len(files)
	image_var=[]
	frames = []
	width = 500
	height = 500
	count =1
	temp_image = Image.new("1", (width, height), (255))
	out_scale = random.randint(1,10) * 10 
	distort = random.randint(1,10) * 10 

	for x in range(file_count-1):
		image_file = ("frames/"+str (count-1)+'.png')
		new_frame = Image.open(image_file)
		imResize = new_frame.resize((distort, distort), Image.BICUBIC)
		imResize2 = imResize.resize((400-out_scale,400-out_scale), Image.ANTIALIAS)
		imResize2.quantize(colors=256)
		imResize2 = imResize2.convert('P', palette=imResize2.getpalette(), colors=16)
		frames.append(imResize2)
		count = count + 1
	frames[0].save("fade.gif", save_all=True, append_images=frames[1:], duration=250, loop=0,optimize=True)
	print "++++++++++++++++++++++++++++++++++++++++++"
	print "Frames in .gif ==> " + str (file_count)
	print "++++++++++++++++++++++++++++++++++++++++++"
	file_count = 0
