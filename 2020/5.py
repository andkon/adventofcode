# This week I decided I wouldn't keep fighting them.
# I'd just go on with my life.
# Maybe I could return some stuff to ease the financial burden.
# And every day, there's a new one of these.
# Am I okay? I can be if I act as though I really am.


# It's a binary space partition. Neato.
# First 7 characters name one of 127 rows, with F or B.
# Last 3 characters name the seat, with L or R
# Then there's a unique seat ID: multiply row by 8, then add the column.


def locate(characters, position=0, r=None):
    if len(characters) == position:
        return r[0]

    direction = characters[position]
    position += 1
    if (direction == "F") or (direction =="L"):
        new_range = r[:len(r)//2]
        return locate(characters, position=position, r=new_range)
    elif (direction == "B") or (direction =="R"):
        new_range = r[len(r)//2:]
        return locate(characters, position=position, r=new_range)

def create_seat_id(row, column):
    math = row * 8 + column
    return math

with open('5.txt', 'r') as reader:
    lines = reader.read()
    bpes = lines.split('\n')

    seat_ids = []

    for bp in bpes:
        print("Boarding pass: %s" % bp)
        row_characters = bp[:7]
        column_characters = bp[7:]
        row = locate(row_characters, r=range(0,128))
        column = locate(column_characters, r=range(0,8))
        seat_ids.append(create_seat_id(row, column))

    seat_ids.sort(reverse=True)
    print("The highest seat ID is %s" % seat_ids[0])
    for seat in seat_ids:
        i = seat_ids.index(seat)
        if seat_ids[i+1] != seat - 1:
            print("Your seat ID is probably %s" % (seat -1))
            break
