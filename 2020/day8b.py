import re


def parse_line(s):
    pattern = r"(\w+) (\+|\-)(\d+)"
    match_group = re.match(pattern, s).groups()
    return (match_group[0], int(match_group[1] + match_group[2]))


def main(l):
    d = {"jmp": "nop", "nop": "jmp"}
    for i in range(len(l)):
        operations = l[:]
        operation, value = operations[i]
        if operation in d:
            operations[i] = (d[operation], value)
        x = execute(operations)
        if x:
            print(x)
            return

def execute(operations):
    visited_operations=set()
    index=0
    accumulator=0
    
    while True:
        if index == len(operations):
            return accumulator
        if index in visited_operations:
            return None
        visited_operations.add(index)
        command, val = operations[index]
        if command == "acc":
            accumulator += val
            index += 1
        elif command == "jmp":
            index += val
        elif command == "nop":
            index += 1


if __name__ == "__main__":
    l = [parse_line(x) for x in open("day8.input.txt").read().split("\n")]
    main(l)
