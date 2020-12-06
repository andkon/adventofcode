# What a beautiful morning.
# My landlord dropped off an anthurium, as a Christmas gift.
# She said she'd put some treats on my door. She has a lot of leftovers.
# The chords I played yesterday sound great today.
# What a beautiful day. What a beautiful day.

# add up the characters that are in every person's answers in a given group
# sum that for all groups

with open('6.txt', 'r') as reader:
    lines = reader.read()
    groups = lines.split('\n\n')

    answer_count = 0

    for group in groups:
        group = group.strip('\n')
        persons = group.split('\n')

        all_characters = group.replace('\n','')
        all_characters = all_characters.strip('\n')

        answered_set = set(all_characters)

        # now let's go through each person
        answers = dict((el, 0) for el in answered_set)

        for person in persons:
            for answer in answered_set:
                if answer in person:
                    answers[answer] += 1

        print(answers)
        print(persons)
        # now add whichever everyone had to the answer count
        for answer, value in answers.items():
            if value == len(persons):
                print("adding 1 from %s for %s" % (answer, persons))
                answer_count += 1

    print("There are %s unique answers" % answer_count)
