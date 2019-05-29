from PIL import Image,ImageDraw
from random import randint as rint
import random
import os





def one_way_loop():
	width = 500
	height = 500
	fraction = 2 # get rid of this 
	frame_scale = 15 # how often to save frames
	back = width/4
	up=9

	color_r = True
	color_b = True
	color_g = True
	img = Image.new("RGB", (width,height), "#FFFFFF")
	img2 = Image.new("RGB", (width,height), "#FFFFFF")
	
	draw = ImageDraw.Draw(img)
	draw2 = ImageDraw.Draw(img2)
	r = random.randint(0, 255) 
	g = random.randint(0, 255) 
	b = random.randint(0, 255) 
	
	count = 0
	color_count = 0
	
	filelist = [ f for f in os.listdir("frames") if f.endswith(".png") ]
	
	for f in filelist:
    		os.remove(os.path.join("frames", f))

	
	for i in range(width/2):
		draw.rectangle((i,i,width-i,height-i), outline=(int(r-i),int(g-i),int(b)))
		draw.rectangle((width/2,height/2,width/2,height/2), outline=(int(r),int(g),int(b)))

	for i in range(width/2):
		draw2.rectangle((i,i,width-i,height-i), outline=(int(r+i),int(g+i),int(b)))
		draw2.rectangle((width/2,height/2,width/2,height/2), outline=(int(r),int(g),int(b)))

	
	for i in range(width/4):
		count = count + 1
		draw.rectangle((i*2,i*2,width-i*2,height-i*2), outline=(int(r+i+1),int(g+i+1),int(b)))
		draw.rectangle((i*2+1,i*2+1,width-i*2-1,height-i*2-1), outline=(int(r+i+1),int(g+i+1),int(b)))
		if 	count % frame_scale == 0 or (count == 1) or (count == 124)  :
			img.save("frames/"+str (count/frame_scale)+".png", "PNG")
			#img.save("frames/"+str (((width/4)/frame_scale)-count/frame_scale)+".png")
	
	for i in range(width/4):
		draw2.rectangle((i*2,i*2,width-i*2,height-i*2), outline=(int(r-i-back),int(g-i-back),int(b)))
		draw2.rectangle((i*2+1,i*2+1,width-i*2-1,height-i*2-1), outline=(int(r-i-back),int(g-i-back),int(b)))
		if 	count % frame_scale == 0 or (count == 1)or (count == 499):
			img2.save("frames/"+str (up*2-count/frame_scale)+".png", "PNG")
			#img.save("frames/"+str (((width/4)/frame_scale)-count/frame_scale)+".png")
		count = count - 1


def two_way_loop():	
	width = 500
	height = 500
	fraction = 2 # get rid of this 
	frame_scale = 15 # how often to save frames
	back = width/4
	up=9

	color_r = True
	color_b = True
	color_g = True
	img = Image.new("RGB", (width,height), "#FFFFFF")
	img2 = Image.new("RGB", (width,height), "#FFFFFF")
	
	draw = ImageDraw.Draw(img)
	draw2 = ImageDraw.Draw(img2)
	r = random.randint(0, 255) 
	g = random.randint(0, 255) 
	b = random.randint(0, 255) 
	
	count = 0
	color_count = 0
	
	filelist = [ f for f in os.listdir("frames") if f.endswith(".png") ]
	
	for f in filelist:
    		os.remove(os.path.join("frames", f))

	
	for i in range(width/2):
		draw.rectangle((i,i,width-i,height-i), outline=(int(r-i),int(g-i),int(b)))
		draw.rectangle((width/2,height/2,width/2,height/2), outline=(int(r),int(g),int(b)))

	for i in range(width/2):
		draw2.rectangle((i,i,width-i,height-i), outline=(int(r-i),int(g-i),int(b)))
		draw2.rectangle((width/2,height/2,width/2,height/2), outline=(int(r),int(g),int(b)))

	
	for i in range(width/4):
		count = count + 1
		draw.rectangle((i*2,i*2,width-i*2,height-i*2), outline=(int(r+i+1),int(g+i+1),int(b)))
		draw.rectangle((i*2+1,i*2+1,width-i*2-1,height-i*2-1), outline=(int(r+i+1),int(g+i+1),int(b)))
		if 	count % frame_scale == 0 or (count == 1) or (count == 124)  :
			img.save("frames/"+str (count/frame_scale)+".png", "PNG")
			#img.save("frames/"+str (((width/4)/frame_scale)-count/frame_scale)+".png")
	
	for i in range(width/4):
		draw2.rectangle((i*2,i*2,width-i*2,height-i*2), outline=(int(r+i+1),int(g+i+1),int(b)))
		draw2.rectangle((i*2+1,i*2+1,width-i*2-1,height-i*2-1), outline=(int(r+i+1),int(g+i+1),int(b)))
		if 	count % frame_scale == 0 or (count == 1)or (count == 499):
			img2.save("frames/"+str (up+count/frame_scale)+".png", "PNG")
			#img.save("frames/"+str (((width/4)/frame_scale)-count/frame_scale)+".png")
		count = count - 1
	



	


def dup():
	path, dirs, files = next(os.walk("frames"))
	file_count = len(files)
	count = 0
	#reverse_frame =0

	#for file in os.listdir("frames"):

	for i in range(file_count):
	
		reverse_frame = (file_count*2) - count
		image_file = Image.open("frames/"+str (count)+".png")
		image_file.save("frames/"+str (reverse_frame-3) +".png", "PNG")
		count = count +1









