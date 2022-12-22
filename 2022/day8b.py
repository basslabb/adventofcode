import math


def create_grid(l):
    grid = []
    for y in l:
        grid.append([int(x) for x in y])
    return grid


def get_viewing_distance(current_value, trees):
    distance = 0
    for index in range(0, len(trees)):
        distance = index+1
        tree = trees[index]
        if current_value <= tree:
            break
    return distance


def get_scenic_score(x, y, grid):
    current_value = grid[y][x]
    vertical_values = ([grid[_y][x] for _y in range(y+1, len(grid))], [
        grid[_y][x] for _y in range(y-1, -1, -1)])
    horizontal_values = ([grid[y][_x] for _x in range(x+1, len(grid[y]))], [
                         grid[y][_x] for _x in range(x-1, -1, -1)])
    viewing_distances = math.prod([*[get_viewing_distance(current_value, x) for x in vertical_values], *[
        get_viewing_distance(current_value, x) for x in horizontal_values]])
    return viewing_distances


def main(l):
    grid = create_grid(l)
    scenic_scores = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            scenic_scores.append(get_scenic_score(x, y, grid))

    print(max(scenic_scores))


if __name__ == "__main__":
    s = """30373
25512
65332
33549
35390"""
    #l = s.split("\n")
    l = open("day8.input.txt").read().split("\n")
    main(l)
