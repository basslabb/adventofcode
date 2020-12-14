from collections import defaultdict
import re
def main(programs: defaultdict(list)):
    memory = defaultdict(int)
    for bit_mask, operations in programs.items():
        bit_mask_values = [(index, value) for index, value in enumerate(bit_mask) if value != "X"]
        for mem_address, value in operations:
            bin_value = "{0:{fill}36b}".format(value, fill='0')
            for index,c in bit_mask_values:
                bin_value = bin_value[:index] + c + bin_value[index+1:]
            new_value = int(bin_value, 2)
            memory[mem_address] = new_value
    print(sum([v for k,v in memory.items()]))


def parse_line(lines):
    d = defaultdict(list)
    current_key = None
    for line in lines:
        if line[0:4] == "mask":
            current_key = line.split("=")[1].strip()
        else:
            mem_address, value = tuple([int(x) for x in re.match(r"mem\[(\d+)\] = (\d+)", line).groups()])
            d[current_key].append((mem_address, value))
    return d

if __name__ == "__main__":
    programs = parse_line(open("day14.input.txt").read().split("\n"))
    main(programs)