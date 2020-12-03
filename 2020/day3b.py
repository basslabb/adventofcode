from math import prod


def main(l, slope):
    pos = (0, 0)
    trees = 0
    while pos[1] < len(l):
        row = l[pos[1]]
        cell = row[pos[0]]
        if cell == "#":
            trees += 1
        pos = (pos[0] + slope[0], pos[1] + slope[1])
    return trees


if __name__ == "__main__":
    slopes = [(1, 1,), (3, 1), (5, 1), (7, 1), (1, 2)]
    l = [x * 100 for x in open("day3.input.txt").read().split("\n")]
    # l = [x * 100 for x in ["..##.......",
    #                        "#...#...#..",
    #                        ".#....#..#.",
    #                        "..#.#...#.#",
    #                        ".#...##..#.",
    #                        "..#.##.....",
    #                        ".#.#.#....#",
    #                        ".#........#",
    #                        "#.##...#...",
    #                        "#...##....#",
    #                        ".#..#...#.#"]]

    print(prod([main(l, x) for x in slopes]))
