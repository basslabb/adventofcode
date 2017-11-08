with open("day1input.txt") as r:
	input = [i.strip() for i in r.read().split(",")]

start_position = [0,0]
position = [0,0]
current_direction = "N"

for i in input:
	if current_direction == 'N':
		if i[0:1] == "L":
			position[0] -= int(i[1:])
			current_direction = 'W'
			continue
		if i[0:1] == "R":
			position[0] += int(i[1:])
			current_direction = 'E'
			continue
	if current_direction == 'S':
		if i[0:1] == "L":
			position[0] += int(i[1:])
			current_direction = 'E'
			continue
		if i[0:1] == "R":
			position[0] -= int(i[1:])
			current_direction = 'W'
			continue
	if current_direction == 'W':
		if i[0:1] == "L":
			position[1] -= int(i[1:])
			current_direction = 'S'
			continue
		if i[0:1] == "R":
			position[1] += int(i[1:])
			current_direction = 'N'
			continue
	if current_direction == 'E':
		if i[0:1] == "L":
			position[1] += int(i[1:])
			current_direction = 'N'
			continue
		if i[0:1] == "R":
			position[1] -= int(i[1:])
			current_direction = 'S'
			continue
	print("Position after: ", position)
print((start_position[0]-position[0]) + (start_position[1]-position[1]))