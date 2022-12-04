def get_range(range_string):
    start, end = [int(x) for x in range_string.split("-")]
    return list(range(start, end+1))


def main(l):
    fully_contained = 0
    for pair in l:
        first_range, second_range = [get_range(x) for x in pair.split(",")]
        if all(x in second_range for x in first_range) or all(x in first_range for x in second_range):
            fully_contained += 1
    print(fully_contained)


if __name__ == "__main__":
    s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    #l = s.split("\n")
    l = open("day4.input.txt").read().split("\n")
    main(l)
