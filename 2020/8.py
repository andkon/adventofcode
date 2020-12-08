# Doing these puzzles feels like the biggest waste of time.
# Like, I already am moving like molasses. I've already wasted so much time.
# And here I am, doing something just because I want to?
# How dare I, when I have so much to do? When so much is unknown?

# 8.txt has one instruction per line of text.
# Follow them until you run an instruction a second time
# then print the accumulator's value.

with open('8.txt', 'r') as reader:
    txt = reader.read()
    txt = txt.strip()
    instructions = txt.split('\n')

    seen_lines = []

    position = 0
    acc = 0

    while True:
        instr, value = instructions[position].split(' ')
        value = int(value)
        print("%s: %s %s" % (position, instr, value))

        if position in seen_lines:
            print("Already seen: %s" % position)
            break
        else:
            seen_lines.append(position)

        if instr == "acc":
            position += 1
            acc += value
        elif instr == "jmp":
            position += value
        elif instr == "nop":
            position += 1

    print("Total is: %s" % acc)
