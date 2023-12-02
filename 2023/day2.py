def set_is_possbible(raw_sets, configuration):
	possible = True
	for sets in raw_sets:
		values = [[value for value in set.strip().split(" ")] for set in sets.split(",")]
		for value, color in values:
			if int(value) > configuration[color]:
				possible = False
				break
	return possible



def main(l, configuration):
	possible_games = []
	for game in l:
		game_id = int(game[0].split(" ")[1])
		if set_is_possbible(game[1].split(";"), configuration):
			possible_games.append(game_id)
	print(sum(possible_games))
			

if __name__ == "__main__":
	s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
	
	configuration = {
	"blue": 14,
	"green": 13,
	"red": 12
	}
	#l = [x.split(":") for x in s.split("\n")]
	l = [x.split(":") for x in open("day2.input.txt").read().split("\n")]
	main(l, configuration)
