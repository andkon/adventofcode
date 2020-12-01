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
import unittest

def third(number):
	""" Returns the number of steps between number and 1 in that weird data table structure. 
	Pretty sure this doesn't actually work well at all... It's off by 1?
	"""
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

"""
the next version is different.
You fill in the squares in the same order
But the value is the sum of all adjacent squares: the 8 squares surrounding the spot you're trying to fill.

I don't think you can cheat in the same way you did above. I think you need to build it. I wish I'd taken some notes!
Maybe I can store things in a dict?
{x,y} where x and y are positions from 0
And all I have to figure out is the next value after

Not sure what a good strategy is here. Nor a good data structure. 
"""

class CircleStruct(object):
	"""
	1. gets a value to return a greater value than
	2. we call find_next_value(input_value)
	3. we start a for loop that keeps running fill_square until the input_value is surpassed
	"""
	def __init__(self):
		super(CircleStruct, self).__init__()
		self.data = {(0,0): 1}

	def find_next_value(self, input_value):
		""" We call this. It does the coordinating, the hard work, to find the value after input_value """
		# First, we need to build out the square.
		return self.fill_square_until(input_value)

	""" Filling methods """
	def fill_square_until(self, value):
		""" Keeps expanding the square until it hits value """
		last_value = 0
		print("First: %s" % (value))
		last_coordinate = (0,0)
		while last_value <= value:
			# keep a fillin'
			print("Last: %s \n" % (last_value))
			last_coordinate, last_value = self.fill_next_square(last_coordinate)
		return last_value


	def fill_next_square(self, coordinate):
		""" Takes a coordinate tuple, adds the next value to self.data """
		if self.data.get(coordinate):
			# there actually is that coordinate
			# now we decide how it should move
			# now we figure out if there's something above
			next_coordinate = self.find_next_square(coordinate, filled_okay=False)
			print(next_coordinate)
			try:
				value = self.data[next_coordinate]
				return next_coordinate, value
			except KeyError:
				# we still gotta fill it
				self.data[next_coordinate] = self.surrounding_sum_finder(next_coordinate)
				return next_coordinate, self.data[next_coordinate]

	def find_next_square(self, coordinate, filled_okay=False):
		""" Finds the actual next square, whether filled or not. 
		returns a tup : (x,y)
		"""
		if filled_okay==True:
			# Honestly just find the next higher number
			coordinate_value = self.keys[coordinate]
			# TODO: well okay, this won't work. we need to flip it around and reverse it
			# so that keys become values, and values become keys
			# then sort the values from lo to hi
			# then see what (x,y) is associated with it
			backwards = {v:k for k,v in a.items()}
			lo_to_hi = sorted(list(c.values()))
			for val in lo_to_hi:
				if val > coordinate_value:
					return backwards[val]
		else:
			# more complicated shit oyyyy
			# basically, you need to figure out which direction we're going
			# and what's around you
			"""
			fill right if there's:
			1. nothing to the right.
			2. nothing below.
			3. something to the left.
			4. something above.

			fill up if there's:
			1. nothing above
			2. nothing to the right
			3. something to the left

			fill left if there's:
			1. nothing to the left.
			2. nothing above.
			3. something to the right.
			4. something below.

			flil down if there's:
			1. nothing below
			2. nothing left
			3. something to the right.
			"""
			x, y = coordinate
			# the problem is obviously here. 
			if len(self.data) == 1:
				return (1,0)
			elif self.data.get((x+1, y)): # something right
				if self.data.get((x, y-1)): #something below
					return (x-1,y)
				else: # nothing below
					return (x, y-1)
			elif self.data.get((x-1, y)): #something_left
				if self.data.get((x, y+1)): # something above
					return (x+1, y)
				else: # nothing above
					return (x,y+1)
			else: #nothing left or right
				# check if top left or top right, we're on a corner
				if self.data.get((x-1,y-1)): #top right
					return (x-1, y)
				elif self.data.get((x+1, y+1)): # we're in bottom left
					return (x+1, y)


	""" Summing methods """
	def surrounding_sum_finder(self, coordinate):
		""" Find the sum of all the surrounding values in the data structure """
		permutations = [
			(1,1), # top right
			(-1,-1), # bottom left
			(1,0), # right
			(-1,0), # left
			(0,1), # top
			(0,-1), # bottom
			(1,-1), # bottom right
			(-1,1) # top left
		]

		a = 0
		for x in permutations:
			try:
				a = a+self.data[(coordinate[0]+x[0],coordinate[1]+x[1])]
			except:
				pass
		return a


class MyTest(unittest.TestCase):
	""" run tests by just running `python first.py` """
	def setUp(self):
		self.puzzle_input=277678

	def test_first_star(self):
		# first star
		self.assertEqual(third(13), 4)
		self.assertEqual(third(3), 2)
		self.assertEqual(third(self.puzzle_input), 475)

	def test_second_star(self):
		c = CircleStruct()
		self.assertEqual(c.find_next_value(2),4)
		c1=CircleStruct()
		self.assertEqual(c1.find_next_value(4),5)
	def test_second_star_1(self):
		c = CircleStruct()
		self.assertEqual(c.find_next_value(25),26)
		c1 = CircleStruct()
		self.assertEqual(c1.find_next_value(59),122)
		c2 = CircleStruct()
		self.assertEqual(c2.find_next_value(147),304)
		# self.assertGreater(c.find_next_value(self.puzzle_input), self.puzzle_input)

	def text_second_star_lol(self):
		self.assertEqual(c2.find_next_value(277678), 279138)


if __name__ == "__main__":
	unittest.main()