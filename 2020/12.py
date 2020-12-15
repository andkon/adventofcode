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

position = (0,0)
direction = "E"

def travel_direction(position, direction, distance):
    if direction == "N":
        position = (position[0], position[1] + distance)
    elif direction == "S":
        position = (position[0], position[1] - distance)
    elif direction == "E":
        position = (position[0] + distance, position[1])
    elif direction == "W":
        position = (position[0] - distance, position[1])
    return position

for x in xs:
    instruction = x[:1]
    distance = int(x[1:])

    # now let's walk through them
    if instruction in RIGHT_DIRECTIONS:
        position = travel_direction(position, instruction, distance)
    elif instruction == "L":
        # doesn't move, just changes direction
        current_heading_index = LEFT_DIRECTION.index(direction)
        new_heading_index = ((distance // 90) + current_heading_index) % len(LEFT_DIRECTION)
        direction = LEFT_DIRECTION[new_heading_index]
    elif instruction == "R":
        current_heading_index = RIGHT_DIRECTIONS.index(direction)
        new_heading_index = ((distance // 90) + current_heading_index) % len(RIGHT_DIRECTIONS)
        direction = RIGHT_DIRECTIONS[new_heading_index]
    elif instruction == "F":
        position = travel_direction(position, direction, distance)

print("Distance: ", calculate_distance((0,0), position))
