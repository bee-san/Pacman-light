#!/usr/bin/env python

import unicornhat as unicorn
import time
import math
import colorsys
import random


r, g, b = random.randint(1,255), random.randint(1,255), random.randint(1,255)
# multiple assignments, assigns R, G, B to their colours

def cooldown(unicorn):
	# function which lowers the unicorn hat brightness
		for y in range(500, 11, -1):
			# counts down from 500 to 11 (below 10 it flickers)
			time.sleep(0.001)
			# waits this long before carrying on
			if y < 100:
				# 0.050 instead of 0.500 again
				y = "0.0" + str(y)
			else:
				# 0.500
				y = "0." + str(y)
				# nifty string manipulation
			y = float(y)
			# makes string into float
			unicorn.brightness(y)
			unicorn.show()
			# changes brightness and shows it


while True:
	unicorn.brightness(0.001)
	for y in range(8):
		for x in range(8):
			unicorn.set_pixel(x,y,int(r),int(g),int(b))
			# creates the 64 pixel grid, assigns the combo of R, G and B to the grid
			# this makes the color


	for x in range(0, 500):
		# this slowly brightens up the display and shows the colors, stops it from flashing
		time.sleep(0.001)
		if x < 100:
			x = "0.00" + str(x)
		else:
			x = "0." + str(x)
		x = float(x)
		unicorn.brightness(x)
		unicorn.show()


	time.sleep(5)
	# waits 5 seconds on one full colour
	cooldown(unicorn)

	r += 30
	if r >= 255:
		r = random.randint(1,255)

	g += 30
	if g >= 255:
		g = random.randint(1,255)

	b += 30
	if b >= 255:
		b = random.randint(1,255)
	# makes sure the colours dont go over 255, which will break everything