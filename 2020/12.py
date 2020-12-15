import fileinput

# Getting back to what's good for you is harder when you're hearing you aren't deserving.
# There are many ways I've heard that in the past. Many ways now I hear its echo.
# And something good for me can feel like a threat in that light.
# If I refuse the message of my inadequacy, and act as though I really deserve better,
# how will I be hurt next?

# Calculate the ship's manhattan distance from all the instructions.

RIGHT_DIRECTIONS = ["N", "E", "S", "W"] # clockwise / right
LEFT_DIRECTION = ["N", "W", "S", "E"] # counterclockwise / left

xs = [x.strip() for x in list(fileinput.input())]

def calculate_distance(beginning, end):
    x = abs(beginning[0]) + abs(end[0])
    y = abs(beginning[1]) + abs(end[1])
    return x + y

wpos = (10,1)
spos = (0,0)
# direction = "E"

def move_waypoint(wpos, direction, distance):
    if direction == "N":
        wpos = (wpos[0], wpos[1] + distance)
    elif direction == "S":
        wpos = (wpos[0], wpos[1] - distance)
    elif direction == "E":
        wpos = (wpos[0] + distance, wpos[1])
    elif direction == "W":
        wpos = (wpos[0] - distance, wpos[1])
    return wpos

def rotate_waypoint(wpos, direction, degrees):
    rotations = degrees // 90

    index_to_negate = 0
    if direction == "R":
        index_to_negate = 1

    i = 0

    while i < rotations:
        reverse = list(wpos[::-1])
        reverse[index_to_negate] = reverse[index_to_negate] * -1
        wpos = tuple(reverse)
        i += 1

    # print(wpos)
    return wpos


for x in xs:
    instruction = x[:1]
    distance = int(x[1:])

    # now let's walk through them
    if instruction in RIGHT_DIRECTIONS:
        # move the waypoint
        wpos = move_waypoint(wpos, instruction, distance)
    elif instruction == "L":
        # L90 would be
        # (10, 4) east 10, north 4
        # (-4, 10) yup, rotate and minus the 1st value
        wpos = rotate_waypoint(wpos, "L", distance)
    elif instruction == "R":
        # rotates the waypoint around the ship
        # R90 would be:
        # (10, 4) east 10, north 4
        # (4, -10) east 4, south 10
        # (-10, -4) west 10, south 4
        # (-4, 10) west 4, north 10
        # for each 90, flip, then negate the 2nd value
        wpos = rotate_waypoint(wpos, "R", distance)
    elif instruction == "F":
        # move the ship in the waypoint's orientation * distance
        wpos_x = wpos[0] * distance
        wpos_y = wpos[1] * distance
        spos = (spos[0] + (wpos[0] * distance), spos[1] + (wpos[1] * distance))
    # print(wpos, spos)

print("Distance: ", calculate_distance((0,0), spos))
