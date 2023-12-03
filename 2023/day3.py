import re

def is_adjacent_to_symbol(x,y, grid):
	x_values = [x-1, x, x+1]
	y_values = [y-1, y, y+1]
	values = []
	for _y in y_values:
		for _x in x_values:
			if _y in range(0, len(grid)) and _x in range(0,len(grid[_y])) and (x,y) != (_x,_y):
				values.append(grid[_y][_x])
	return ([value for value in values if not value.isnumeric() and value != '.'])

def main(grid):
	part_numbers = []
	current_number = ""
	is_adjacent = False
	for y in range(0, len(grid)):
		for x in range(0, len(grid[y])):
			value = grid[y][x]
			if value.isnumeric():
				current_number += value
				if not is_adjacent:
					is_adjacent = is_adjacent_to_symbol(x,y, grid)
			else:
				if current_number != "" and is_adjacent:
					part_numbers.append(int(current_number))
				current_number = ""
				is_adjacent = False
	print(sum(part_numbers))
				
				

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
