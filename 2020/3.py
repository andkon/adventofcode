# I don't need to do anything fancy. Just write out what works, then make it better
# Over time, what matters stays.

# Whenever the downstairs door opens here I'm still afraid of who might be coming in.
# But it is easier here. It's easier to notice the fear, and it takes less time to realize I'm safe.

# Starting in the top left, move right three and down one. Count how many trees you hit.

def navigate(m, right, down):
    trees_hit = 0
    current_row = 0
    current_position = 0

    while current_row < (len(m) - 1):
        if m[current_row][current_position % 31] == "#":
            trees_hit += 1
        current_row += 1
        current_position += 3

    return (trees_hit, current_position, current_row)

with open('3.txt', 'r') as reader:
    the_map = reader.read()
    rows = the_map.split('\n')

    info = navigate(rows, 3, 1)
    print("You hit %s and navigated %s positions and %s rows" % (info[0], info[1], info[2]))
