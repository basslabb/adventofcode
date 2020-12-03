def main(l):
    pos = (0, 0)
    trees = 0
    while pos[1] < len(l):
        row = l[pos[1]]
        cell = row[pos[0]]
        if cell == "#":
            trees += 1
        pos = (pos[0] + 3, pos[1] + 1)
    print(trees)


if __name__ == "__main__":
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
    main(l)
