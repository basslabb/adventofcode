def rotate_row(l, i):
    return l[-i:] + l[:-i]

def rotate_column(column_id, grid, steps):
    column = [grid[i][column_id] for i in range(0, 6)]
    column_row = rotate_row(column, steps)
    for i in range(0, len(grid)):
        grid[i][column_id] = column_row[i]

def parse_commands(s, grid):
    l = s.split()
    c = l[0]
    if c == "rect":
        x,y = l[1].split("x")
        x, y = int(x), int(y)
        for i in range(0, x):
            for j in range(0, y):
                grid[j][i] = "X"
    elif c == "rotate":
        to_rotate = l[1]
        steps = int(l[4])
        if to_rotate == "column":
            column_id = int(l[2].split("=")[1])
            rotate_column(column_id, grid, steps)
        elif to_rotate == "row":
            row_id = int(l[2].split("=")[1])
            grid[row_id] = rotate_row(grid[row_id], steps)

def print_message(grid):
    for row in grid:
        print(''.join(row))

def main(l):
    grid = []
    for i in range(0,6):
        grid.append(["." for i in range(0, 50)])
    for i in l:
        parse_commands(i, grid)
    lit = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "X":
                lit += 1
    print(lit)
    print(grid)
    print_message(grid)

if __name__ == '__main__':
    l = open("day8input.txt").read().split("\n")
    #print(rotate([1,2,3,4,5]))
    main(l)