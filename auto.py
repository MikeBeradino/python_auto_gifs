try:
	import Image
except ImportError:
	from PIL import Image
import random
import argparse

p = argparse.ArgumentParser(description="Generate an elementary cellular automaton")
p.add_argument("-x", "--width", help="Width", default=22)
p.add_argument("-y", "--height", help="Height", default=22)
p.add_argument("-r", "--rulenumber", help="Rule number", default=18)
p.add_argument("-o", "--outputfile", help="Output file", default="out.png")
p.add_argument("-s", "--scalefactor", help="Scale the output image by an interger amount", default=1)
args = p.parse_args()

width = int(args.width)
height = int(args.height)
rulenumber = int(args.rulenumber)
scalefactor = int(args.scalefactor)

count = 0

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
		
		new.save(args.outputfile+str (count)+".png",)
		new.putpixel((x, y), true_pixel if ca[int(y/scalefactor)][int(x/scalefactor)] else false_pixel)
		#new.save(args.outputfile+str (x)+".png",)
		

print("Saving image...")
#new.save(args.outputfile)
print("Done!")
