try:
	import Image
except ImportError:
	from PIL import Image, ImageSequence
import random
import argparse
import os
from resizeimage import resizeimage
path, dirs, files = next(os.walk("dir2"))
file_count = len(files)
image_var=[]
frames = []
frames_reverse = []


for x in range(file_count-1):
	
	image_file = ("dir2/"+str (x+1)+'.png')
	new_frame = Image.open(image_file)
	frames.append(new_frame)


frames[0].save("1_foward.gif", save_all=True, append_images=frames[0:], duration=1, loop=0)

im = Image.open('1_foward.gif')

frames_reverse = [frames_reverse.copy() for frames_reverse in ImageSequence.Iterator(im)]
frames_reverse.reverse()


frames_reverse.extend(frames)
frames_reverse[0].save('1_reversed.gif', save_all=True, append_images=frames_reverse[1:], duration=1, loop=0)

print(file_count)
print("Saving image...")
#new.save(args.outputfile)
print("Done!")
