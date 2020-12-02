# Y'know, last time I played this I was very fried, and pushing harder and harder
# It makes sense I blew up my achilles a month later
# It makes sense I met Val then and made things work

# This is about validating each password against a policy.
# Return the count of how many passwords are valid.

# make tuples of passwords and policies
# call a "validate" function
# checks that the relevant letter can only be found more than or equal to x but less than or equal to y times
# increment a count, and return that


def validate(tup):
    # return 1 if valid
    # return 0 if not
    rule = tup[0]
    password = tup[1]

    rule_count, rule_letter = rule.split(" ")

    rule_min, rule_max = [ int(x) for x in rule_count.split("-") ]

    count_of_letter = password.count(rule_letter)

    if rule_min <= count_of_letter <= rule_max:
        return 1
    else:
        return 0


with open('2.txt', 'r') as reader:
    text = reader.read()
    lines = text.split("\n")

    combos = [ tuple(x.split(": ")) for x in lines if x.strip() ]

    count = 0
    for combo in combos:
        count += validate(combo)

    print(count)
