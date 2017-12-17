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

from functools import reduce

def reverse_captcha(numbers):
	st = str(numbers)
	digits = list(st)
	for i in range(len(digits)):
		digits[i] = int(digits[i])
	print(digits)

	first = digits[0]
	final = digits[-1]

	print(first, " ", final)

	current_position = 0
	summable_numbers = []

	for current_number in digits:
		try:
			last_number = digits[current_position-1]
			if current_number == last_number:
				# add it to summable
				summable_numbers.append(current_number)

			elif current_position+1 == len(digits):
				# if the last number is equal to the first number
				# then add it
				summable_numbers.append()
		except:
			pass

		current_position+=1

	try:
		total_sum = reduce(lambda a,x: a+x, summable_numbers)
		return total_sum
	except:
		return 0
