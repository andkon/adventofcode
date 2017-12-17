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
import unittest


def reverse_captcha(numbers, offset=1):
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


class MyTest(unittest.TestCase):
	""" run tests by just running `python first.py` """
	def setUp(self):
		self.big_number=428122498997587283996116951397957933569136949848379417125362532269869461185743113733992331379856446362482129646556286611543756564275715359874924898113424472782974789464348626278532936228881786273586278886575828239366794429223317476722337424399239986153675275924113322561873814364451339186918813451685263192891627186769818128715595715444565444581514677521874935942913547121751851631373316122491471564697731298951989511917272684335463436218283261962158671266625299188764589814518793576375629163896349665312991285776595142146261792244475721782941364787968924537841698538288459355159783985638187254653851864874544584878999193242641611859756728634623853475638478923744471563845635468173824196684361934269459459124269196811512927442662761563824323621758785866391424778683599179447845595931928589255935953295111937431266815352781399967295389339626178664148415561175386725992469782888757942558362117938629369129439717427474416851628121191639355646394276451847131182652486561415942815818785884559193483878139351841633366398788657844396925423217662517356486193821341454889283266691224778723833397914224396722559593959125317175899594685524852419495793389481831354787287452367145661829287518771631939314683137722493531318181315216342994141683484111969476952946378314883421677952397588613562958741328987734565492378977396431481215983656814486518865642645612413945129485464979535991675776338786758997128124651311153182816188924935186361813797251997643992686294724699281969473142721116432968216434977684138184481963845141486793996476793954226225885432422654394439882842163295458549755137247614338991879966665925466545111899714943716571113326479432925939227996799951279485722836754457737668191845914566732285928453781818792236447816127492445993945894435692799839217467253986218213131249786833333936332257795191937942688668182629489191693154184177398186462481316834678733713614889439352976144726162214648922159719979143735815478633912633185334529484779322818611438194522292278787653763328944421516569181178517915745625295158611636365253948455727653672922299582352766484

	def test(self):
		# first star
		self.assertEqual(reverse_captcha(1122), 3)
		self.assertEqual(reverse_captcha(1111), 4)
		self.assertEqual(reverse_captcha(1234), 0)
		self.assertEqual(reverse_captcha(91212129), 9)
		self.assertEqual(reverse_captcha(self.big_number), 1034)

		# second star
		self.assertEqual(reverse_halfway(1212), 6)
		self.assertEqual(reverse_halfway(1221), 0)
		self.assertEqual(reverse_halfway(123425), 4)
		self.assertEqual(reverse_halfway(123123), 12)
		self.assertEqual(reverse_halfway(12131415), 4)
		self.assertEqual(reverse_halfway(self.big_number),1356)


if __name__ == "__main__":
	unittest.main()