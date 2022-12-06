import re


def main(crates, instructions):
    stacks = {i: []
              for i in range(0, len(re.findall("[0-9]", crates.split("\n")[-1])))}
    for i in crates.split("\n")[:-1]:
        for j in range(0, len(i), 4):
            index = j//4
            if i[j:j+4].strip() != "":
                stacks[index].insert(0, i[j:j+4])

    for i in instructions.split("\n"):
        quantity, from_stack, to_stack = [
            int(x) for x in re.findall("[0-9]+", i)]
        for index in range(0, quantity):
            value = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(value)

    print("".join(re.findall(
        "[A-Z]", "".join([stacks[key][-1].strip() for key in stacks]))))


if __name__ == "__main__":
    s = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    #l = s.split("\n\n")
    l = open("day5.input.txt").read().split("\n\n")
    main(*l)
