
def get_direction(current_direction, direction):
    if current_direction == "N" and direction == "L":
        current_direction = "W"
    elif current_direction == "N" and direction == "R":
        current_direction = "E"
    elif current_direction == "S" and direction == "L":
        current_direction = "E"
    elif current_direction == "S" and direction == "R":
        current_direction = "W"
    elif current_direction == "W" and direction == "L":
        current_direction = "S"
    elif current_direction == "W" and direction == "R":
        current_direction = "N"
    elif current_direction == "E" and direction == "L":
        current_direction = "N"
    elif current_direction == "E" and direction == "R":
        current_direction = "S"
    return current_direction

def main(l):
    start_position = [0, 0]
    position = [0, 0]
    current_direction = "N"
    visited = []
    already_visited = None
    for i in l:
        d, steps = i[0:1], int(i[1:])
        original_direction = current_direction
        current_direction = get_direction(current_direction, d)
        for j in range(0, steps):
            if [position[0], position[1]] in visited and already_visited is None:
                already_visited = [position[0], position[1]]
            visited.append([position[0], position[1]])
            if current_direction == "N":
                position[1] += 1
            elif current_direction == "S":
                position[1] -= 1
            elif current_direction == "E":
                position[0] += 1
            elif current_direction == "W":
                position[0] -= 1
    print((start_position[0]-already_visited[0]) + (start_position[1]-already_visited[1]))

if __name__ == '__main__':
    l = [i.strip() for i in open("day1input.txt").read().split(",")]
    main(l)
