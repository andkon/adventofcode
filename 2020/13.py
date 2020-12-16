import fileinput

# There is so much that fits in a python file.
# I lived for a long time trying to be okay with fitting less and less of myself
# in a smaller and smaller space.
# And now that I'm noticing how much has been missing,
# I'm letting myself put things where I didn't think they were allowed to be.
# A comment is ignored by the interpreter, but that doesn't mean it's nothing.
# Just because a computer wouldn't understand it doesn't make it worthless.
# Just because you have to translate what you want doesn't make your wanting irrelevant.
# It makes it all the more important, actually.

# look at the first line to get your arrival timestamp
# get the list of buses - their associated number is the frequency they arrive
# What's the ID of the first bus you could take, multipled by the number of minutes you have to wait?

xs = [x.strip() for x in list(fileinput.input())]

arrival_time = int(xs[0])
buses = map(lambda x: int(x), filter(lambda x: x != "x", xs[1].split(',')))

earliest_bus = 0
earliest_wait = 10000
for bus_id in buses:
    if arrival_time % bus_id == 0:
        # perfecto
        earliest_bus = bus_id
        earliest_wait = 0
        print("earliest bus (perfect): ", bus_id, earliest_wait)
        break
    elif (arrival_time / float(bus_id)) > (arrival_time // bus_id):
        # it arrives shortly before the arrival_time
        previous_bus_time = arrival_time - (arrival_time % bus_id)
        next_time = previous_bus_time + bus_id
        if next_time - arrival_time < earliest_wait:
            earliest_wait = next_time - arrival_time
            earliest_bus = bus_id
            print("earliest bus (before): ", bus_id)
    elif (arrival_time / float(bus_id)) < (arrival_time // bus_id):
        # it arrives after the arrival_time
        next_time = arrival_time + (arrival_time % bus_id)
        if next_time - arrival_time < earliest_wait:
            earliest_wait = next_time - arrival_time
            earliest_bus = bus_id
            print("earliest bus (after): ", bus_id, earliest_wait)

print(earliest_bus*earliest_wait)
