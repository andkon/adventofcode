import fileinput

# There is only so much that fits in a python file.
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
# part 2
# make the list of positions to check relative to the biggest number, and what to % them by
ys = [] # [(relative_index, bus_id)]

full_buses = xs[1].split(',')

for i, bus_id in enumerate(full_buses):
    if bus_id == "x":
        full_buses[i] = 0
    else:
        full_buses[i] = int(bus_id)

print(full_buses)
biggest_bus_index = full_buses.index(max(full_buses))
print(biggest_bus_index)

for i, bus_id in enumerate(full_buses):
    ys.append((i-biggest_bus_index, bus_id))

time = 0
missing = False
found_count = 0

highest_found_count = (0,0)

incrementable = full_buses[biggest_bus_index]
last_time = 0
while True:
    # print(time)
    for y in ys:
        y_time = time + y[0]

        try:
            if y_time < 0:
                missing = True
                break
            elif y_time % y[1] != 0:
                # import pdb; pdb.set_trace()
                missing = True
                break
            else:
                found_count+=1
        except ZeroDivisionError:
            found_count+= 1
            # it's an inactive route
            # as long as it's greater than zero we're good
            # print(e, " - ", time + y[0])
    if missing==True:
        # iterate and keep on

        print("Found %s at %s" % (found_count, time))
        if found_count > 0:
            # import pdb; pdb.set_trace()
            if highest_found_count[0] == found_count:
                # we've seen it before
                # let's make sure we're setting the right incrementable

                gap = time - highest_found_count[1]
                # import pdb; pdb.set_trace()
                if gap > incrementable:
                    incrementable = gap
                    highest_found_count = (found_count, time)
                    print("Seen before but new gap!", found_count, "Incrementable is now ", incrementable)
                else:
                    highest_found_count = (found_count, time)
            elif found_count > highest_found_count[0]:
                # we haven't seen this, but it's higher
                # don't increase the gap, just set it to be higher
                highest_found_count = (found_count, time)

        last_time = time
        time += incrementable
        missing = False
        found_count = 0

    else:
        print("Ding ding: ", time + ys[0][0])
        break
