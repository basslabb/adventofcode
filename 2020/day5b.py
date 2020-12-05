def to_binary(s):
    d = {"F": "0","B": "1","R": "1","L": "0"}
    return d[s]


def main(l):
    seats = [] 
    for i in l:
        row,column = (int("".join([to_binary(x) for x in i[:7]]), 2), int("".join([to_binary(x) for x in i[7:]]), 2))
        seat_id = row * 8 + column
        seats.append(seat_id)
    sorted_seats = sorted(seats)
    print([x for x in range(sorted_seats[0], sorted_seats[-1]+1) if x not in sorted_seats][0])


if __name__ == "__main__":
    l = open("day5.input.txt").read().split("\n")
    #l = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    main(l)
