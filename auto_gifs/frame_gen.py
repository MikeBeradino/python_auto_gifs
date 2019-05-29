from PIL import Image,ImageDraw
from random import randint as rint
import random
import os

width = 500
height = 500
fraction = 2 # get rid of this 
frame_scale = 15 # how often to save frames

color_r = True
color_b = True
color_g = True

filelist = [ f for f in os.listdir("frames") if f.endswith(".png") ]
for f in filelist:
    os.remove(os.path.join("frames", f))


def random_gradient(name):
	img = Image.new("RGB", (width,height), "#FFFFFF")
	draw = ImageDraw.Draw(img)
	r = random.randint(0, 255) 
	g = random.randint(0, 255) 
	b = random.randint(0, 255) 
	count = 0
	color_count = 0

	
	for i in range(width/2):
		draw.rectangle((i,i,width-i,height-i), outline=(int(r-i),int(g-i),int(b)))
		draw.rectangle((width/2,height/2,width/2,height/2), outline=(int(r-60),int(g-60),int(b-6020)))

	
	for i in range(width/4):
		count = count + 1
		draw.rectangle((i*2,i*2,width-i*2,height-i*2), outline=(int(r+i+1),int(g+i+1),int(b)))
		draw.rectangle((i*2+1,i*2+1,width-i*2-1,height-i*2-1), outline=(int(r+i+1),int(g+i+1),int(b)))
		if 	count % frame_scale == 0 or (count == 1):
			img.save("frames/"+str (count/frame_scale)+".png", "PNG")
			#img.save("frames/"+str (((width/4)/frame_scale)-count/frame_scale)+".png")

		color_count = color_count + 1
		
		if color_count == width:
			color_count = 0
			
			if r >= color_scale and color_r == True:
				r = r - (color_scale) 
			
			if r <= color_scale:
				color_r = False
			
			if color_r == False:
				r = r + (color_scale)
			
			if r > 255 - color_scale and color_r == False:
				color_r = True

			if g >= color_scale and color_g == True:
				g = g - (color_scale) 
			if g <= color_scale:
				color_g = False
			if color_g == False:
				g = g + (color_scale)
			if g > 255 - color_scale and color_g == False:
				color_g = True

			if b >= color_scale and color_b == True:
				b = b - (color_scale) 
			if b <= color_scale:
				color_b = False
			if color_b == False:
				b = b + (color_scale)
			if b > 255 - color_scale and color_b == False:
				color_b = True


   

if __name__ == "__main__":
	for name in range(1):
		random_gradient(str(name))






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
	#print(file_count)
	#print(count)
