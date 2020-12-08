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

    # loop through each instruction.
    # swap jmp/nop
    # try it out

    for i, instruction in enumerate(instructions):
        instruples = []
        # make the tuples
        for x, instruction in enumerate(instructions):
            instr, value = instructions[x].split(' ')
            value = int(value)
            t = (instr, value)
            instruples.append(t)

        print(instruples)
        row_to_change = instruples[i]
        if row_to_change[0] == "jmp":
            instruples[i] = ("nop", value)
        elif row_to_change[0] == "nop":
            instruples[i] = ("jmp", value)
        print(instruples)


        seen_lines = []

        position = 0
        acc = 0
        solved = False

        while True:
            try:
                instr, value = instruples[position]
                print("%s: %s %s" % (position, instr, value))
            except IndexError:
                print("This nightmare is over! We are free! %s" % acc)
                solved = True
                break

            if position in seen_lines:
                print("Already seen: %s" % position)
                acc = 0
                position = 0
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
        if solved == True:
            print("Total is: %s" % acc)
            break
