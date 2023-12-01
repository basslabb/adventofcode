import re

numbers_map = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
	"eight":8,"nine":9}

numbers_text = "|".join([x for x in numbers_map.keys()])

def map_numbers_to_digits(s):
	if s in numbers_map.keys():
		return str(numbers_map[s])
	return s

def main(l):
	_sum = 0
	for i in range(0, len(l)):
		numbers_list = l[i]
		first,last = map_numbers_to_digits(numbers_list[0]),map_numbers_to_digits(numbers_list[-1])
		_sum += int(first + last)
	print(_sum)

if __name__ == "__main__":
	s = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
	#l = [re.findall(rf"(?=([0-9]|{numbers_text}))",x) for x in s.split("\n")]
	l = [re.findall(rf"(?=([0-9]|{numbers_text}))",x) for x in open("day1.input.txt").read().split("\n")]
	main(l)
