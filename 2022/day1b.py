def main(l):
    sums = []
    for i in l:
        sums.append(sum([int(j) for j in i]))
    sorted_sums = sorted(sums, reverse=True)
    print("top three sums:", sum(sorted_sums[:3]))


if __name__ == "__main__":
    s = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    l = [x.split("\n") for x in open("day1.input.txt").read().split("\n\n")]
    #l = [x.split("\n") for x in s.split("\n\n")]

    main(l)
