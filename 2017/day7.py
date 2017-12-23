def get_line_data(line):
    left = line[0:line.index(" ")]
    if "->" in line:
        right = line.split("->")[1]
        right = [str(x).strip() for x in right.split(",")]
    else:
        right = []
    return (left, right)

def main(l):
    root = None
    d = {get_line_data(i)[0]:get_line_data(i)[1] for i in l}
    keys = set(d.keys())
    values = set([item for sublist in list(d.values()) for item in sublist])
    for i in keys:
        if i not in values:
            root = i
    print(root)

if __name__ == '__main__':
    l = open("day7.input.txt").read().split("\n")
    main(l)