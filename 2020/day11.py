def main(l):
    grid = l
    while True:
        new_grid = step(grid)
        if new_grid == grid:
            print(''.join(grid).count('#'))
            break
        grid = new_grid

def step(l):
    new_grid = []
    for y in range(len(l)):
        new_row = ""
        for x in range(len(l[y])):
            current_seat = l[y][x]
            positions = get_adjacent_positions(x, y, len(l[y]), len(l))
            seat_status = get_adjacent_seat_status(positions, l)
            seat_status_availability = [s for _x, _y, s in seat_status]
            if  current_seat == "L" and seat_status_availability.count("#") == 0:
                new_row += "#"
            elif current_seat == "#" and seat_status_availability.count("#") >=4:
                new_row += "L"
            else:
                new_row += current_seat
        new_grid.append(new_row)
    return new_grid


def get_adjacent_seat_status(positions, grid):
    l = []
    for x, y in positions:
        if x == -1 or y == -1 or x >= len(grid[0]) or y >= len(grid):
            l.append((x, y, "L"))
            continue
        if grid[y][x] == "L":
            l.append((x, y, "L"))
        elif grid[y][x] == "#":
            l.append((x, y, "#"))
    return l

def get_adjacent_positions(x, y, max_x, max_y):
     positions = []
     for i in range(x-1, x+2):
         for j in range(y-1, y+2):
            positions.append((i, j))
     return [(_x,_y) for _x,_y in positions if (_x,_y) != (x,y)]

if __name__ == "__main__":
    l = [list(x) for x in open("day11.input.txt").read().split("\n")]
    main(l)