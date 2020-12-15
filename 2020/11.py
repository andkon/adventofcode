import fileinput
from functools import reduce
import copy
# It feels safe to try. To use your big old brain to find the best way.
# The best way might be safe.
# It never turns out to be so clear.
# And the only thing that you learn, over and over again, is that trying to be okay comes at a cost.
# At the cost of being you.

POSITIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
)
# look at the positions surrounding all seats, simultaneously:
# if the seat is empty ("L") and no occupied seats are adjacent, it becomes occupied.
# if 4 or more adjacent seats are occupied, it becomes empty.
rows = [list(x.strip()) for x in list(fileinput.input())]

first_seats = {} # key is a (x,y) coordinate, value is a list of tuples of other coordinates

def find_visible_seats(rows, row, seat):
    visible_seats = []

    # solve the algo here
    for position in POSITIONS:
        # these are the directions it keeps iterating over
        current_coordinates = (row,seat)

        while True:
            try:
                next_row = current_coordinates[0]+position[0]
                if next_row < 0 or next_row > len(rows):
                    break
                next_seat = current_coordinates[1]+position[1]
                if (next_seat < 0) or (next_seat > len(rows[0])):
                    break
                next_coordinates = (next_row, next_seat)
                next_value = rows[next_coordinates[0]][next_coordinates[1]]
                if next_value != ".":
                    visible_seats.append(next_coordinates)
                    break
                current_coordinates = next_coordinates
            except IndexError:
                break
    return(visible_seats)



def check_visible_seats(rows, coordinate_tuple):
    # returns a boring ol' array of the actual values at the given coordinates
    seats = []
    visible_seats = first_seats[coordinate_tuple]

    for position in visible_seats:
        new_seat = rows[position[0]][position[1]]
        if new_seat != ".":
            seats.append(new_seat)
    return seats


for (i, row) in enumerate(rows):
    for (x, seat) in enumerate(row):

        first_seats[(i, x)] = find_visible_seats(rows, row=i, seat=x)

old_rows = copy.deepcopy(rows)
new_rows = []
generation = 0
empty_seats = 0
occupied_seats = 0
while old_rows != new_rows:
    if len(new_rows) > 0:
        old_rows = new_rows
        empty_seats = 0
        occupied_seats = 0
        generation += 1
    new_rows = [ [ "" for x in range(len(old_rows[0]))] for _ in range(len(old_rows))]
    # I htink I replace old_rows here
    for (i, row) in enumerate(old_rows):
        for (s, seat) in enumerate(row):
            if seat == ".":
                new_rows[i][s] = "."

            visible_seats = check_visible_seats(old_rows, (i, s))

            if seat == "L":
                # check if none of the seats are occupied
                if "#" not in visible_seats:
                    new_rows[i][s] = "#"
                    occupied_seats += 1
                else:
                    new_rows[i][s] = "L"
                    empty_seats += 1
            elif seat == "#":
                # currently occupied
                if visible_seats.count("#") >= 5:
                    new_rows[i][s] = "L"
                    empty_seats += 1
                else:
                    new_rows[i][s] = "#"
                    occupied_seats += 1

print("This many generations: ", generation)
print("occupied seats: ", occupied_seats)
