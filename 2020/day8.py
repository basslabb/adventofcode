import re


def parse_line(s):
    pattern = r"(\w+) (\+|\-)(\d+)"
    match_group = re.match(pattern, s).groups()
    return (match_group[0], int(match_group[1] + match_group[2]))


def main(l):
    print(execute(l))


def execute(operations, index=0, visited_operations=set(), accumulator=0):
    if index in visited_operations:
        return accumulator
    command, val = operations[index]
    new_index, new_accumulator = map_operation(
        (command, val), index, accumulator)
    visited_operations.add(index)
    return execute(operations, new_index, visited_operations, new_accumulator)


def map_operation(operation, index, accumulator):
    command, val = operation
    if command == "acc":
        accumulator += val
        index += 1
    elif command == "jmp":
        index += val
    elif command == "nop":
        index += 1
    return index, accumulator


if __name__ == "__main__":
    l = [parse_line(x) for x in open("day8.input.txt").read().split("\n")]
    s = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    #l = [parse_line(x) for x in s.split("\n")]
    main(l)
