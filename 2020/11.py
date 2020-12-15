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

def get_adjacent_seats(rows, row=0, seat=0):
    seats = []
    for position in POSITIONS:
        try:
            r = row + position[0]
            s = seat + position[1]
            if (r >= 0) and (s >= 0):
                new_seat = rows[row + position[0]][seat + position[1]]
                if new_seat != ".":
                    seats.append(new_seat)
        except IndexError:
            pass
    return seats

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
            adjacent_seats = get_adjacent_seats(old_rows, row=i, seat=s)
            # import pdb; pdb.set_trace()
            if seat == "L":
                # check if none of the seats are occupied
                if "#" not in adjacent_seats:
                    new_rows[i][s] = "#"
                    occupied_seats += 1
                else:
                    new_rows[i][s] = "L"
                    empty_seats += 1
            elif seat == "#":
                # currently occupied
                if adjacent_seats.count("#") >= 4:
                    new_rows[i][s] = "L"
                    empty_seats += 1
                else:
                    new_rows[i][s] = "#"
                    occupied_seats += 1

print("This many generations: ", generation)
print("occupied seats: ", occupied_seats)
