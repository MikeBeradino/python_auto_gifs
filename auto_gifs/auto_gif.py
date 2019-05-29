import pytumblr
from frame_gen import (two_way_loop,dup,one_way_loop)
from frames2gif import frames2gifs
from post2tumbler import post2
import random
import time
import sys, select
from blend_images import (blend_ends,blend_mid)
loop = False
sleep = 60 # in min
master_counter = 1
print "++++++++++++++++++++++++++++++++++++++++++"
start = raw_input('Start auto gifs y/n ?: ')
print "++++++++++++++++++++++++++++++++++++++++++"
if start == "y":
	loop = True 
while loop == True:
	random_loop = random.randint(0,1)
	if random_loop == 0:
		two_way_loop()
	else:
		one_way_loop()
		blend_mid()
		blend_ends()
	frames2gifs()
	post2()
	
	random_time = random.randint(10 ,60) * sleep
 	print "++++++++++++++++++++++++++++++++++++++++++"
 	print "Made " + str (master_counter) + " .Gif"
	print "++++++++++++++++++++++++++++++++++++++++++"
	print "Press enter to quit..next post in "+ str (random_time/60) + " min"
	print "++++++++++++++++++++++++++++++++++++++++++"
	i, o, e = select.select( [sys.stdin], [], [], random_time )
	if (i):
		print "++++++++++++++++++++++++++++++++++++++++++"
  		print "Goodbye"
  		print "++++++++++++++++++++++++++++++++++++++++++"
  		loop = False
	else:
		print "++++++++++++++++++++++++++++++++++++++++++"
  		print "Making more art"
  		print "++++++++++++++++++++++++++++++++++++++++++"

  	master_counter = master_counter + 1


    	
