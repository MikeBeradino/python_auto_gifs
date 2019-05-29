import pytumblr
from frame_gen import (two_way_loop,dup,one_way_loop)
from frames2gif import frames2gifs
from post2tumbler import post2
import random
import time
import sys, select
from blend_images import (blend_ends,blend_mid)


loop = False
sleep = 1
random_time = random.randint(30,60) * sleep

#time.sleep(random_time)

start = raw_input('start_bot y/n ?: ')
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
	
	random_time = random.randint(3,6) * sleep
	print("sleep",random_time)

	#quit = raw_input('quit y/n ?: ')	
	#if quit == "y":
		#loop = False

	print "Press enter to quit..You have ten seconds"
	i, o, e = select.select( [sys.stdin], [], [], 10 )
	if (i):
  		print "goodbye"
  		loop = False
	else:
  		print "making more art"



    	
