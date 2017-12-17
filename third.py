"""
third day is fucked

Basic problem:
1. Figure out what number is at what x,y position.
1.5. Figure out where 1 is located.
2. Just return the difference between it and 1.

So you kinda need an equation here to figure out how many different numbers
are in each

okay.
every layer's number of positions is easy to figure out:
1 (sqrt of 1)
9 (sqrt of 3)
25 (sqrt is 5)

It's just the square root of the height of each row, minus all the previous positions

SO how do I figure out an arbitrary position? I could just take the sqrt and round up to nearest odd integer
then... well, that number^2 will be the bottom right
oh
this is easy.

then we just count back. so let's say it's...
math.sqrt(13)


"""

import math

def third(number):
	""" Returns the number of steps between number and 1 in that weird data table structure. """
	sq = math.sqrt(number)
	if sq > int(sq):
		final_x = int(sq) + 2
	else:
		final_x = int(sq)

	final_number = final_x**2 

	# now we can cheat a bit! forget calculating position, just figure out difference from the middle
	x_remnant = ((final_number - number) % (final_x -1)) + 1 # tells us the position on the edge
	x_movement = abs(((1+final_x)/2) - x_remnant) # diff between middle x and x_remnant
	print(x_movement)
	y_movement = ((1 + final_x)/2)-1 # tells us how far from the edge it is
	print(y_movement)

	return int(x_movement + y_movement)

