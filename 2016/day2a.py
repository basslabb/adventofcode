with open("day2input.txt") as f:
	lines = f.read().split("\n")

key_pad = [[1,2,3],[4,5,6],[7,8,9]]

pos = 5
visited_pos = [5]
print(lines)
code = []
for line in lines:
	_pos = pos
	for c in line:
		print(c, _pos)
		if c == "R" and _pos not in (3,6,9):
			_pos+=1
		elif c == "L" and _pos not in (1,4,7):
			_pos-=1
		elif c == "U" and _pos not in (1,2,3):
			_pos-=3
		elif c == "D" and _pos not in (7,8,9):
			_pos+=3
	code.append(_pos)

print(code)
print(pos)