import fileinput
# Make a change, and a thousand should follow.
# That's what the vulnerable feeling is about:
# How much might I get lost in all those changes?
# And that's scarier when you're barely there to begin with.


# you have a bunch of joltage adapters, with a specific output joltage.
# they can TAKE 1, 2 or 3 jolts lower than its output rating & still output the rated joltage
# also, your device can take 3 jolts higher than the highest adapter in your bag.
# the charging outlet's joltage rating is 0.

# Use every adapter at once, and find out the gap in each step between the outlet, adapters, and device.
# multiply the number of one jolt differences by the number of 3 jolt differences

# the device: highest adapter + 3
# adapters: start with lowest, pick next based on lowest that still is only 1, 2 or 3 higher
# the outlet: 0. Start there!

adapters = [int(x) for x in list(fileinput.input())]
adapters = sorted(adapters)

differences = {}
last_jolt = 0

adapters.sort()

for adapter in adapters:
    difference = adapter - last_jolt
    differences[difference] = differences.get(difference, 0) + 1
    last_jolt = adapter

differences[3] = differences[3] + 1

builtin = adapters[-1] + 3
print("Your built-in adapter is %s" % builtin)
print("The first solution is: ", differences[1] * differences[3])

# # make the tuples connecting everything
# edges = []
adapters.insert(0, 0)
adapters.append(builtin)

DP = {}
def dp(i):
    if i==len(adapters)-1: # if you're already at the end, you're done. There's just one way to get there.
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(adapters)): # here's the dumb brute force part: just try each next adapter
        if adapters[j]-adapters[i]<=3: # you can get to the next answer if it's less than three away
            # first, step to j, then we iterate j
            # this actually recursively steps through EACH FOLLOWING ADAPTER
            # like, it starts at index 0 + 1
            # We accumulate the TOTAL NUMBER OF SOLUTIONS in ans, not the actual huge ass array of the paths
            ans += dp(j)
            # but that's expensive as hell and exhausting (exponential!) to do every time. So we'll also make a dict, DP
            # and store up the ans for each index
            # it's basically going through len(adapters) * len(adapters) # of times.
    DP[i] = ans
    return ans


# the algorithmic idea here:
# https://www.youtube.com/watch?v=cE88K2kFZn0&feature=youtu.be
# how many ways to go through the whole list? including skipping?
# we solve this with dynamic programming
# What's DP? You write down a recursive brute force solution.
# that's this function: dp(i): the number of ways to complete the adapter given that you are at adapter[i]

print(dp(0)) # start with index 0
