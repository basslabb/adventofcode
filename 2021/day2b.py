def move(direction, value, current_pos):
    aim = current_pos[2]
    match direction:
        case "down":
            return [0, 0, value]
        case "up":
            return [0, 0, -value]
        case "forward":
            return [value, value*aim, 0]


def main(l):
    pos = [0, 0, 0]
    for i in l:
        direction, value = i.split(" ")
        new_pos = move(direction, int(value), pos)
        pos = [pos[0]+new_pos[0], pos[1]+new_pos[1], pos[2]+new_pos[2]]

    print(pos[0]*pos[1])


if __name__ == "__main__":
    s = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    l = open("day2.input.txt").read().split("\n")
    #l = s.split("\n")

    main(l)
