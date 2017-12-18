# The spreadsheet consists of rows of apparently-random numbers. 
# To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. 
# For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
# For example, given the following spreadsheet:
# 5 1 9 5
# 7 5 3
# 2 4 6 8
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

defmodule Checksum do
	def checksum_for_spreadsheet(spreadsheet) do
		# spreadsheet is a list of lists
		# it's pass
		prep_spreadsheet(spreadsheet) |> checksum
	end

	defp prep_spreadsheet(spreadsheet_string) do
		# ok split this into rows by newline
		String.split(spreadsheet_string, "\n")
	end

	defp checksum([]) do
		# empty list, so return 0
		0
	end

	defp checksum(rows) do
		# the first call on a list with at least one thing
		# IO.puts("There are " <> Integer.to_string(length(rows)) <> " rows")
		checksum(rows, 0)
	end

	defp checksum([], sum) do
		# the last call - the list is now empty, so return the sum. this is the sum of all lists
		sum
	end

	defp checksum([head | tail], sum) do
		# where we do all the hard work
		# first let's get a list of integers
		row_str = String.split(head)
		row_int = Enum.map(row_str, fn(x) -> String.to_integer(x) end)
		# now, you get the highest and lowest values in the head, which is the row
		# then you get the difference
		# ok maybe we'll do that together
		diff = row_difference(row_int)
		# IO.puts("Now the sum is " <> Integer.to_string(sum + diff))
		checksum(tail, sum+diff) # less ugly by far
	end


	defp row_difference([]) do
		0
	end

	defp row_difference(list) do
		# the starter, the way in. All numbers are positive, so 0 will get replaced in next function.
		# Ah. I do need to pop something in here, to avoid the endless loop of never setting a low.
		# Whoa, drastically simplified
		[first | tail] = list
		row_difference(tail, first, first)
	end

	defp row_difference([head | tail], high, low) when head > high do
		# replace the top value
		row_difference(tail, head, low)
	end

	defp row_difference([head | tail], high, low) when head < low do
		# replace lowest value
		row_difference(tail, high, head)
	end

	defp row_difference([_ | tail], high, low) do
		# here, the head is neither the highest nor the lowest value, so we just abandon it
		row_difference(tail, high, low)
	end

	defp row_difference([], high, low) do
		# IO.puts("The high is " <> Integer.to_string(high) <> " and the low is " <> Integer.to_string(low) <> " with a diff of " <> Integer.to_string(high-low))
		high - low
	end

	# defp row_difference([], high) do
	# 	# there's a high, but not a low (or vice versa). I guess that means a row of one value.
	# 	row_difference([], high, high)
	# end
end

defmodule Modulo do

	defp prep_spreadsheet(spreadsheet_string) do
		# ok split this into rows by newline
		String.split(spreadsheet_string, "\n")
	end

	def modulo_for_spreadsheet(spreadsheet) do
		prep_spreadsheet(spreadsheet) |> modulator
	end


	defp modulator([]) do
		# empty list, so return 0
		0
	end

	defp modulator(rows) do
		# the way in
		IO.puts(">>> There are " <> Integer.to_string(length(rows)) <> " rows to modulate")
		modulator(rows, 0)
	end

	defp modulator([], sum) do
		# final call, return the completed sum
		IO.puts("SUM: #{sum}")
		sum
	end

	defp modulator([head | tail], sum) do
		# doing the hard work, going through rows and summing stuff
		# get list of integers in this row
		row_str = String.split(head)
		row_int = Enum.map(row_str, fn(x) -> String.to_integer(x) end)
		# now we do the math: reorder list by highest number
		high_row = Enum.sort(row_int, &(&1 >= &2))
		low_row = Enum.sort(row_int, &(&1 <= &2))
		summable = find_modulable(high_row, low_row)
		IO.puts("Adding " <> Integer.to_string(summable))
		modulator(tail, sum+summable)
	end

	defp find_modulable([], []) do
		# modulator has passed us a bunch of empty stuff i guess
		0
	end

	defp find_modulable([high_head | high_tail], low_row) do
		# the way in
		find_modulable(high_tail, high_head, low_row, low_row)
	end

	defp find_modulable(high_row, numerator, low_row, [head | tail]) when ((numerator - head) > 0) and (rem(numerator, head) == 0) do
		# yay, break
		IO.puts("#{numerator} / #{head}")
		div(numerator, head)
	end

	defp find_modulable(high_row, numerator, low_row, [head|tail]) do
		find_modulable(high_row, numerator, low_row, tail)
	end

	defp find_modulable(high_row, numerator, low_row, []) do
		# this would happen if we ran out of denominators — meaning no modulable numbers for this numerator
		# time to iterate the high_row, which'll go back to find_modulable/2
		IO.puts("No match for " <> Integer.to_string(numerator))
		find_modulable(high_row, low_row)
	end

 end

# IO.puts(Second.checksum_for_spreadsheet(s1))

ExUnit.start

defmodule AssertionTest do
	use ExUnit.Case, async: true

	setup_all do
		s1="""
			414	382	1515	319	83	1327	116	391	101	749	1388	1046	1427	105	1341	1590
			960	930	192	147	932	621	1139	198	865	820	597	165	232	417	19	183
			3379	987	190	3844	1245	1503	3151	3349	2844	4033	175	3625	3565	179	3938	184
			116	51	32	155	102	92	65	42	48	91	74	69	52	89	20	143
			221	781	819	121	821	839	95	117	626	127	559	803	779	543	44	369
			199	2556	93	1101	122	124	2714	625	2432	1839	2700	2636	118	2306	1616	2799
			56	804	52	881	1409	47	246	1368	1371	583	49	1352	976	400	1276	1240
			1189	73	148	1089	93	76	3205	3440	3627	92	853	95	3314	3551	2929	3626
			702	169	492	167	712	488	357	414	187	278	87	150	19	818	178	686
			140	2220	1961	1014	2204	2173	1513	2225	443	123	148	580	833	1473	137	245
			662	213	1234	199	1353	1358	1408	235	917	1395	1347	194	565	179	768	650
			119	137	1908	1324	1085	661	1557	1661	1828	1865	432	110	658	821	1740	145
			1594	222	4140	963	209	2782	180	2591	4390	244	4328	3748	4535	192	157	3817
			334	275	395	128	347	118	353	281	430	156	312	386	160	194	63	141
			146	1116	153	815	2212	2070	599	3018	2640	47	125	2292	165	2348	2694	184
			1704	2194	1753	146	2063	1668	1280	615	163	190	2269	1856	150	158	2250	2459
		"""
		{:ok, spreadsheet: s1}
	end

	test "first star", state do
		s2 = """
		5 1 9 5
		7 5 3
		2 4 6 8
		"""
		assert Checksum.checksum_for_spreadsheet(state[:spreadsheet]) == 30994
		assert Checksum.checksum_for_spreadsheet(s2) == 18
	end

	test "second star",state do
		s2 = """
		5 9 2 8
		9 4 7 3
		3 8 6 5
		"""

		assert Modulo.modulo_for_spreadsheet(s2) == 9
		assert Modulo.modulo_for_spreadsheet(state[:spreadsheet]) == 1
	end
end