# http://adventofcode.com/2017/day/6
import unittest

def redistribute_highest(memory):
	m = max(memory)
	max_indices = [i for i,j in enumerate(memory) if j == m]
	index = max_indices[0]

	# get and set that position
	redistribute = memory[index]
	memory[index] = 0

	next_index = (index+1) % len(memory)
	while redistribute > 0:
		memory[next_index] +=1
		redistribute -= 1
		next_index = (next_index+1) % len(memory)
	return memory


def cycle_memory(s):
	memory_strings = s.split("\t")
	memory = list((int(x) for x in memory_strings))

	count = 0
	results = []
	seen = None
	while True:
		memory = redistribute_highest(memory)
		count += 1
		if memory in results:
			if seen != False:
				count = count - results.index(memory) - 1
				break
			else:
				seen = True

		results.append(list(memory))

	print("Final count: %s" % count)
	return count




class MyTest(unittest.TestCase):
	""" run tests by just running `python first.py` """
	def setUp(self):
		self.test = "0	2	7	0"
		self.puzzle = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"

	def test_first_star_test(self):
		# first star
		self.assertEqual(cycle_memory(self.test),4)

	def test_first_star_puzzle(self):
		self.assertGreater(cycle_memory(self.puzzle),1)


if __name__ == "__main__":
	unittest.main()
