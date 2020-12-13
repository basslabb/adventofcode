def main(l):
    grid = l
    iteration = 1
    while True:
        new_grid = step(grid)
        if new_grid == grid:
            print(''.join(grid).count('#'))
            break
        grid = new_grid
        iteration += 1
        

def step(l):
    directions = ["up", "down", "left", "right", "up_left", "up_right", "down_left", "down_right"]
    new_grid = []
    for y in range(len(l)):
        new_row = ""
        for x in range(len(l[y])):
            current_seat = l[y][x]
            positions = [get_adjacent_seat(x, y, l, direction) for direction in directions]
            positions = [x for x in positions if x is not None]
            seat_status = get_adjacent_seat_status(positions, l)
            seat_status_availability = [s for _x, _y, s in seat_status]
            if  current_seat == "L" and seat_status_availability.count("#") == 0:
                new_row += "#"
            elif current_seat == "#" and seat_status_availability.count("#") >=5:
                new_row += "L"
            else:
                new_row += current_seat
        new_grid.append(new_row)
    return new_grid


def get_adjacent_seat_status(positions, grid):
    l = []
    for x, y in positions:
        if grid[y][x] == "L":
            l.append((x, y, "L"))
        elif grid[y][x] == "#":
            l.append((x, y, "#"))
    return l

def get_adjacent_seat(x, y, grid, direction):
    d = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0), "up_left": (-1, 1), 
        "up_right": (1, 1), "down_left": (-1, -1), "down_right": (1, -1)}
    _direction = d[direction]
    _x, _y = (x + _direction[0], y + _direction[1])
    max_x, max_y = len(grid[0]),len(grid)
    while -1 < _x < max_x and -1 < _y < max_y:
        if _x == x and _y == y:
            continue
        if grid[_y][_x] != ".":
            return (_x, _y)
        _x += _direction[0]
        _y +=_direction[1]
    return None

if __name__ == "__main__":
    l = [list(x) for x in open("day11.input.txt").read().split("\n")]
    main(l)