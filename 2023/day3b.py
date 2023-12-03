import math

def is_adjacent_to_gear(x,y, grid):
	x_values = [x-1, x, x+1]
	y_values = [y-1, y, y+1]
	positions = []
	for _y in y_values:
		for _x in x_values:
			if _y in range(0, len(grid)) and _x in range(0,len(grid[_y])) and (x,y) != (_x,_y):
				positions.append((_x,_y))
	gear = [(_x,_y) for _x,_y in positions if grid[_y][_x] == '*']
	return  gear[0] if len(gear) > 0 else None

def main(grid):
	current_number = ""
	gear_position = None
	gears = {}
	for y in range(0, len(grid)):
		for x in range(0, len(grid[y])):
			value = grid[y][x]
			if value.isnumeric():
				current_number += value
				if not gear_position:
					gear_position = is_adjacent_to_gear(x,y, grid)
			else:
				if current_number != "" and gear_position:
					if gear_position in gears:
						gears[gear_position].append(int(current_number))
					else:
						gears[gear_position] = [int(current_number)]
				current_number = ""
				gear_position = None
	print(sum([math.prod(values) for _,values in gears.items() if len(values) > 1]))
	
				
				

if __name__ == "__main__":
	s = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
	
	#l = [list(line) for line in s.split("\n")]
	l = [list(line) for line in open("day3.input.txt").read().split("\n")]
	main(l)
