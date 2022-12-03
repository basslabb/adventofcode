import re


def calculate_priority(character):
    if re.match("[a-z]", character):
        return ord(character) - 96
    return ord(character) - 38


def main(l):
    sums = []
    for i in range(0, len(l), 3):
        first = l[i]
        second = l[i+1]
        third = l[i+2]
        in_all = list(set([x for x in first if x in second and x in third]))
        sums.append(sum(calculate_priority(x) for x in in_all))

    print(sum(sums))


if __name__ == "__main__":
    s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    #l = s.split("\n")
    l = open("day3.input.txt").read().split("\n")
    main(l)
