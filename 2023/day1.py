import re

def main(l):
	digits = [int(x[0] + x[-1]) for x in l]
	print(sum(digits))

if __name__ == "__main__":
	s = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
	#l = ["".join(re.findall(r"[0-9]+",x)) for x in s.split("\n")]
	l = ["".join(re.findall(r"[0-9]+",x)) for x in open("day1.input.txt").read().split("\n")]
	main(l)
