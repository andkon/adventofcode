# What a beautiful morning.
# My landlord dropped off an anthurium, as a Christmas gift.
# She said she'd put some treats on my door. She has a lot of leftovers.
# The chords I played yesterday sound great today.
# What a beautiful day. What a beautiful day.

# add up the unique characters in each group
# sum the count of unique characters for all groups



with open('6.txt', 'r') as reader:
    lines = reader.read()
    groups = lines.split('\n\n')

    answer_count = 0

    for group in groups:
        group = group.replace('\n','')
        group = group.strip('\n')
        answer_count += len(set(group))

    print("There are %s unique answers" % answer_count)
