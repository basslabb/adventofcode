import re
import collections


def parse_bag(s):
    regex = r"(?:\d )(\w+ \w+)(?: bags?)"
    match = re.match(regex, s)
    if match is None:
        return None
    return match.groups()[0]


def parse_bag_string(s):
    container_bag, y = s.split("contain ")
    regex = r"(\w+ \w+)(?: bags?)"
    match = re.fullmatch(regex, container_bag.strip())

    if match is None:
        return None

    bags = [parse_bag(x.strip()) for x in y.split(",")]
    return (match.groups()[0], bags)


contained_in = collections.defaultdict(set)
has_gold = set()


def main(l):
    for i in l:
        bag = parse_bag_string(i)
        if bag is not None:
            print(bag)
            for j in bag[1]:
                contained_in[j].add(bag[0])
    num = 0
    traverse("shiny gold")
    print(len(has_gold))


def traverse(color):
    for i in contained_in[color]:
        if i is not None:
            has_gold.add(i)
            traverse(i)


if __name__ == "__main__":
    l = open("day7.input.txt").read().split("\n")
    main(l)
