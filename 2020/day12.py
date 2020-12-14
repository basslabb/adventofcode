import re

def main(l):
    direction = "E"
    positions = [(0,0)]
    for i in l:
        direction, new_pos = move(direction, i, positions[-1])
        positions.append(new_pos)
    last = positions[-1]
    print(abs(last[0]) + abs(last[1]))
    

def move(direction, instruction, pos):
    action, value = instruction
    action = direction if action == "F" else action
    d = {"N": (pos[0], pos[1]+value), "S": (pos[0], pos[1]-value), "E": (pos[0] + value, pos[1]), "W": (pos[0]-value, pos[1])}
    new_pos = pos
    cardinal_directions = ["N", "E", "S", "W"]
    if action in d:
        new_pos = d[action]
    else:
        index = cardinal_directions.index(direction)
        new_index = index + ((value if action == 'R' else -value) // 90)
        new_index = new_index % len(cardinal_directions) if new_index >= len(cardinal_directions) else new_index
        direction = cardinal_directions[new_index]
    return direction, new_pos

def parse_line(s):
    match = re.match(r"(\w)(\d+)", s).groups()
    return (match[0], int(match[1]))


if __name__ == "__main__":
    l = [parse_line(x) for x in open("day12.input.txt").read().split("\n")]
    s = """F10
N3
F7
R90
F11"""
    #l = [parse_line(x) for x in s.split("\n")]
    #l = s.split("\n")
    main(l)