"""
ADVENT OF CODE 1 2017
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. 
The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
What is the solution to your captcha?

split into [a,b], then check if x[1] matches y[0]
"""
import math
from functools import reduce

def reverse_captcha(numbers, offset):
	""" String of numbers, where it sums them if it matches the digit at the position indicated by offset """

	# Turn string of numbers into digits
	st = str(numbers)
	digits = list(st)
	for i in range(len(digits)):
		digits[i] = int(digits[i])
	print(digits)

	current_position = 0
	summable_numbers = []


	for current_number in digits:
		# Let's try not checking the last number
		try:
			next_number = digits[(current_position+offset) % len(digits)]
			if current_number == next_number:
				print("At position %s, the number %s matches the number %s positions ahead" % (current_position, current_number, offset))
				# add it to summable
				summable_numbers.append(current_number)
		except:
			raise

		current_position+=1

	try:
		total_sum = reduce(lambda a,x: a+x, summable_numbers)
		return total_sum
	except:
		return 0

def reverse_halfway(numbers):
	""" Same as above, but instead of setting an offset, it finds the number halfway aroun the list.
	e.g. a list with 10 items would have an offset of 10/2 = 5 
	"""
	# Turn string of numbers into digits
	st = str(numbers)
	digits = list(st)
	for i in range(len(digits)):
		digits[i] = int(digits[i])
	print(digits)

	current_position = 0
	summable_numbers = []

	offset = (len(digits) + 2 // 2) // 2
	print("List is %s long, so offset is %s" % (len(digits), offset))


	for current_number in digits:
		# Let's try not checking the last number
		try:
			next_number = digits[(current_position+offset) % len(digits)]
			if current_number == next_number:
				print("At position %s, the number %s matches the number %s positions ahead" % (current_position, current_number, offset))
				# add it to summable
				summable_numbers.append(current_number)
		except:
			raise

		current_position+=1

	try:
		total_sum = reduce(lambda a,x: a+x, summable_numbers)
		return total_sum
	except:
		return 0
