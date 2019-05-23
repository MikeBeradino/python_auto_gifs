try:
	import Image
except ImportError:
	from PIL import Image, ImageSequence
import random 
from random import randint as rint
import argparse
import os
from resizeimage import resizeimage

outputfile = ""
width = int(25)
height = int(25)
rulenumber = int(18)
scalefactor = int(1)

color_scale = int (10)

count = 0
color_count = 0

color_r = True
color_b = True
color_g = True

# Define colors of the output image
r = random.randint(0, 255) 
g = random.randint(0, 255) 
b = random.randint(0, 255) 
r1 = random.randint(0, 255) 
g1 = random.randint(0, 255) 
b1 = random.randint(0, 255) 
true_pixel = (r, g, b)
false_pixel = (r1, g1, b1)

# Generates a dictionary that tells you what your state should be based on the rule number and the states of the adjacent cells in the previous generation
def generate_rule(rulenumber):
	rule = {}
	for left in [False, True]:
		for middle in [False, True]:
			for right in [False, True]:
				rule[(left, middle, right)] = rulenumber%2 == 1
				rulenumber //= 2
	return rule

# Generates a 2d representation of the state of the automaton at each generation
def generate_ca(rule):
	ca = []
	# Initialize the first row of ca randomly
	ca.append([])
	for x in range(width):
		ca[0].append(bool(random.getrandbits(1)))

	# Generate the succeeding generation
	# Cells at the eges are initialized randomly
	for y in range(1,height):
		ca.append([])
		ca[y].append(bool(random.getrandbits(1)))
		for x in range(1, width-1):
			ca[y].append(rule[(ca[y-1][x-1], ca[y-1][x], ca[y-1][x+1])])
		ca[y].append(bool(random.getrandbits(1)))
	return ca

rule = generate_rule(rulenumber)
ca = generate_ca(rule)


new = Image.new("RGBA", (width, height), (r1, g1, b1))


print("Placing pixels...")
for y in range(height):
	count = count + 1
	for x in range(width):
		new.save("frames/"+outputfile+str (count)+".png")
		
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
			

		





		new.putpixel((x, y), (r, g, b) 
			if ca[int(y/scalefactor)][int(x/scalefactor)] 
			else (r1, g1, b1))
		#new.save(args.outputfile+str (x)+".png",)
		image = Image.open("frames/"+outputfile+str (count)+".png")
		
		new_image = image.resize((500, 500))
		new_image.save("frames/"+outputfile+str (count)+".png")
		new_image.save("frames/"+outputfile+str ((width*2)-count)+".png")

path, dirs, files = next(os.walk("frames"))
file_count = len(files)
image_var=[]
frames = []
frames_reverse = []

for x in range(file_count-1):
	
	image_file = ("frames/"+str (x+1)+'.png')
	new_frame = Image.open(image_file)
	frames.append(new_frame)

frames[0].save("1_foward.gif", save_all=True, append_images=frames[0:], duration=1, loop=0)
#im = Image.open('1_foward.gif')

#frames_reverse = [frames_reverse.copy() for frames_reverse in ImageSequence.Iterator(im)]
#frames_reverse.reverse()
#frames_reverse.extend(frames)
#frames_reverse[0].save('1_reversed.gif', save_all=True, append_images=frames_reverse[1:], duration=.01, loop=0)

print(file_count)
print("Saving image...")
#new.save(args.outputfile)
print("Done!")
