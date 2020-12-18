def main(o):
    non_valid = []
    rules, tickets = o
    for ticket in tickets:
        for number in ticket:
            valid = any(_min <= number <= _max for _min, _max in rules)
            if not valid:
                non_valid.append(number)
    print(sum(non_valid))


def parse_rule(s):
    rules = []
    for i in s.split("\n"):
        if i == "":
            continue
        rule_string = i.split(":")[1]
        for x in rule_string.split("or"):
            yield tuple([int(y) for y in x.split("-")])


def parse_input(s):
    groups = s.split("\n\n")
    rules = list(parse_rule(groups[0]))
    tickets = [[int(y) for y in x.split(",")]
               for x in groups[2].split("\n")[1:]]
    return (rules, tickets)


if __name__ == "__main__":
    l = parse_input(open("day16.input.txt").read())
    main(l)
