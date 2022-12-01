def main(l):
    sums = []
    for i in l:
        print(",".join(i))
        sums.append(sum([int(j) for j in i]))
    print("max", max(sums))


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
    # print(l)

    main(l)
