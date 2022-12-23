import itertools
from operator import sub, add


def get_motions(s):
    direction, number_of_steps = s.split(" ")
    steps = range(0, int(number_of_steps))
    match direction:
        case 'L':
            return [(-1, 0) for step in steps]
        case 'R':
            return [(1, 0) for step in steps]
        case 'U':
            return [(0, -1) for step in steps]
        case 'D':
            return [(0, 1) for step in steps]


def get_neighbours(pos):
    x, y = pos
    neighbours = []
    for _y in range(y-1, y+2):
        for _x in range(x-1, x+2):
            neighbours.append((_x, _y))
    return neighbours


def main(l):
    motions = list(itertools.chain(*[get_motions(x) for x in l]))
    head_pos = tail_pos = (0, 0)
    tail_visited_positions = [tail_pos]
    for motion in motions:
        prev_mov = head_pos
        head_pos = tuple(map(add, head_pos, motion))
        head_neighbours = get_neighbours(head_pos)
        if tail_pos in head_neighbours:
            continue
        if prev_mov in get_neighbours(tail_pos):
            tail_pos = prev_mov
        else:
            intersect = [x for x in get_neighbours(
                tail_pos) if x in get_neighbours(head_pos)]
            tail_pos = intersect[0]
        tail_visited_positions.append(tail_pos)
    print(
        f"number of positions visited: {len(set(tail_visited_positions))}")


if __name__ == "__main__":
    s = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    #l = s.split("\n")
    l = open("day9.input.txt").read().split("\n")
    main(l)
