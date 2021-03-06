import re
from functools import reduce

import sys
sys.setrecursionlimit(2000)


# What makes this work?
# I just have to read the instructions, and do it.
# That's also what makes it hard.
# Waking up every day, sitting down, and doing a thing I could fail at.
# Looking directly at the instructions is also staring into the abyss.
# The endless emptiness I can lose myself in, hoping to find a sense of salvation.

# take the list of bag rules
# Calculate how many can contain at least one shiny gold bag

# rule_dict = { color: {color1: quantity, color2: quantity}}

SHINY_GOLD = "shiny gold"

def build_dict(rules):
    rule_dict = {}
    for rule in rules:
        # split that into the rule_bag and contents
        rule = rule.replace(" bags", "").strip()
        rule = rule.split(" contain ")
        rule_bag = rule[0]
        rule_dict[rule_bag] = {}

        contents = rule[1].strip('.')

        contents = contents.split(', ')
        for bag in contents:
            quantity, color = bag.split(' ', maxsplit=1)
            color = color.replace(" bag", "").strip()

            if quantity == "no":
                quantity = 0
                rule_dict[rule_bag] = None
            else:
                quantity = int(quantity)
                rule_dict[rule_bag][color] = quantity

    return rule_dict

def get_unique_bags(bag, rule_dict):
    # gets all bags down the chain
    bags = []

    if rule_dict[bag]:
        bags.extend(rule_dict[bag].keys())
        for bag in bags:
            if rule_dict[bag]:
                internal_bags = rule_dict[bag].keys()
                for internal_bag in internal_bags:
                    if internal_bag not in bags:
                        bags.append(internal_bag)
    return bags

def count_up_bags(bag, rule_dict, bags=[], bag_count=0):
    if rule_dict[bag]:
        for color, quantity in rule_dict[bag].items():
            bags.extend((color,)*quantity)
            bag_count += quantity
            print("Bag count before: %s" % bag_count)
    if len(bags) > 0:
        return count_up_bags(bags.pop(0), rule_dict, bags=bags, bag_count=bag_count)
    else:
        return bag_count


with open('7.txt', 'r') as reader:
    txt = reader.read()
    txt = txt.strip()
    rules = txt.split('\n')
    rule_dict = build_dict(rules)

    contains_golden_count = 0
    contains_golden_list = []
    for rule_bag, rule in rule_dict.items():
        # basically recursively iterate through the dict for each new rule_bag we see
        # increment the count and add to the list the moment you see it can contain one shiny gold bag
        if rule in contains_golden_list:
            contains_golden_count += 1
            continue
        # including adding all the rule_bags that've led here - but actually that's optional
        # love it when something turns out to be unnecessary for now

        # but now the hard part: actually checking if any of the contained bags could contain it:
        # recursively make the list of all references
        all_bags = []
        all_bags.extend(get_unique_bags(rule_bag, rule_dict))

        if SHINY_GOLD in all_bags:
            contains_golden_count += 1
            contains_golden_list.append(rule_bag)
    print("Total bags that can contain a golden bag: %s" % contains_golden_count)

    total_bags = count_up_bags(SHINY_GOLD, rule_dict)
    print("Total number of bags in %s: %s" % (SHINY_GOLD, total_bags))
