import re
import collections


def parse_bag(s):
    regex = r"(\d )(\w+ \w+)(?: bags?)"
    match = re.match(regex, s)
    if match is None:
        return None
    return (match.groups()[1], int(match.groups()[0].strip()))


def parse_bag_string(s):
    container_bag, y = s.split("contain ")
    regex = r"(\w+ \w+)(?: bags?)"
    match = re.fullmatch(regex, container_bag.strip())
    if match is None:
        return None
    bags = [parse_bag(x.strip()) for x in y.split(",")]
    return (match.groups()[0], bags)


bags = collections.defaultdict(set)
num = 0

def main(l):
    for i in l:
        bag = parse_bag_string(i)
        if bag is not None:
            for j in bag[1]:
                bags[bag[0]].add(j)
    traverse("shiny gold")
    print(num)

def traverse(color):
    global num
    for i in bags[color]:
        if i is not None:
            for j in range(0, i[1]):
                traverse(i[0])
            num += i[1]


if __name__ == "__main__":
    l = open("day7.input.txt").read().split("\n")
    main(l)
