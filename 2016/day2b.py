with open("day2input.txt") as f:
	lines = f.read().split("\n")
key_pad = [["","","1","",""],["","2","3","4","",],["5","6","7","8","9"], ["","A", "B", "C","",], ["","","D","","",]]
pos = [0,2]
code = []
def get_next_pos(direction):
	next_pos = []
	print(direction)
	if direction == "U":
		next_pos = [0,-1]
	elif direction == "D":
		next_pos = [0,1]
	elif direction == "L":
		next_pos = [-1,0]
	elif direction == "R":
		next_pos = [1,0]
	return next_pos

for line in lines:
	for c in line:
		next_pos = get_next_pos(c)
		print(next_pos)
		if next_pos[0] in key_pad and next_pos[1] in key_pad[next_pos[0]]: #and key_pad[next_pos[0][next_post[1]]] != "" :
			print("tjosan")
			pos[0]+=next_pos[0]
			pos[1]+=next_pos[1]
	code.append(pos)
