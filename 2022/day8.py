def create_grid(l):
    grid = []
    for y in l:
        grid.append([int(x) for x in y])
    return grid


def tree_is_visible(x, y, grid):
    current_value = grid[y][x]
    is_visible = False
    if x == 0 or len(grid[0])-1 == x or y == 0 or len(grid)-1 == y:
        return True

    # vertical
    vertical_values = ([grid[_y][x] for _y in range(y+1, len(grid))], [
        grid[_y][x] for _y in range(y-1, -1, -1)])
    if all(current_value > y for y in vertical_values[0]) or all(current_value > y for y in vertical_values[1]):
        return True
    horizontal_values = ([grid[y][_x] for _x in range(x+1, len(grid[y]))], [
                         grid[y][_x] for _x in range(x-1, -1, -1)])
    if all(current_value > x for x in horizontal_values[0]) or all(current_value > x for x in horizontal_values[1]):
        return True
    return False


def main(l):
    grid = create_grid(l)
    visible_trees = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if tree_is_visible(x, y, grid):
                visible_trees += 1
    print(visible_trees)


if __name__ == "__main__":
    s = """30373
25512
65332
33549
35390"""
    #l = s.split("\n")
    l = open("day8.input.txt").read().split("\n")
    main(l)
