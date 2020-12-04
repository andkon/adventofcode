import re
# Somedays it's extremely hard to get started on anything other than defending myself.
# A cold start is the most terrifying thing.
# On one side, I'm safe from a challenge to myself, my okayness.
# On the other, having worked through it, I've learned both how to do it and that I was okay even if I couldn't.

FIELDS = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
)


# Passwords should contain all the above fields, except for "cid", which I've commented out.
# The passport data in 4.txt is in key:value format, separated by spaces or new lines.
# Passports are separated by blank lines.
# Return the count of how many valid passports

def validate_passport(passport):
    for field in FIELDS:
        try:
            passport[field]
        except KeyError:
            return 0
    return 1


with open('4.txt', 'r') as reader:
    passports_text = reader.read()
    passports = passports_text.split('\n\n')

    valid_count = 0

    for passport in passports:
        passport_terms = re.split("\n| ", passport)
        filtered = filter(lambda x: len(x) > 1, passport_terms)
        passport_dict = dict(s.split(":") for s in filtered)

        valid_count += validate_passport(passport_dict)
    print valid_count
