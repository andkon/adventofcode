import re
# Somedays it's extremely hard to get started on anything other than defending myself.
# A cold start is the most terrifying thing.
# On one side, I'm safe from a challenge to myself, my okayness.
# On the other, having worked through it, I've learned both how to do it and that I was okay even if I couldn't.

FIELDS = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": ((150, 193), (59, 76)),
    "hcl": "^#[0-9a-f]{6}$",
    "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": "^[0-9]{9}$",
    # "cid": ???
}


# Passwords should contain all the above fields, except for "cid", which I've commented out.
# The passport data in 4.txt is in key:value format, separated by spaces or new lines.
# Passports are separated by blank lines.
# Return the count of how many valid passports

def validate_passport(passport):
    print("New passport")
    for key, rule in FIELDS.items():
        # print("Validating %s" % key)
        try:
            value = passport[key]
            # now do the actual validation
            if key in ("byr", "iyr", "eyr"):
                if rule[0] <= int(value) <= rule[1]:
                    print("%s is good" % key)
                else:
                    return 0
            elif key =="hgt":
                if value[-2:] == "cm":
                    cm_rule = rule[0]
                    print(value)
                    int_value = int(value[:-2])
                    if cm_rule[0] <= int_value <= cm_rule[1]:
                        print("It's good")
                    else:
                        return 0
                elif value[-2:] == "in":
                    in_rule = rule[1]
                    int_value = int(value[:-2])
                    if in_rule[0] <= int_value <= in_rule[1]:
                        print("It's good")
                    else:
                        return 0
                else:
                    print("There wasn't a measure on %s" % value)
                    return 0
                print("%s is good" % key)
            elif key =="hcl":
                if not re.match(rule, value):
                    return 0
                print("%s is good" % key)
            elif key =="ecl":
                if value not in rule:
                    return 0
                print("%s is good" % key)
            elif key =="pid":
                if not re.match(rule, value):
                    return 0
                print("%s is good" % key)
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
    print ("There were %s valid passports out of %s" % (valid_count, len(passports)))
