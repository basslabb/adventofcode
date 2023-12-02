def power_of_cubes(raw_sets):
	cubes = {}
	for sets in raw_sets:
		values = [[value for value in set.strip().split(" ")] for set in sets.split(",")]
		for value, color in values:
			if color not in cubes or int(value) > cubes[color]:
				cubes[color] = int(value)
	x,y,z = cubes.values()
	return x*y*z

def main(l):
	sum = 0
	for game in l:
		sum+=(power_of_cubes(game[1].split(";")))
	print(sum)
			

if __name__ == "__main__":
	s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
	
	#l = [x.split(":") for x in s.split("\n")]
	l = [x.split(":") for x in open("day2.input.txt").read().split("\n")]
	main(l)
