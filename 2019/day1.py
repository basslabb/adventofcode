import math

def main(l):
    sum = 0
    for i in l:
        num = int(i)
        res = math.floor(num / 3) - 2
        sum += res
    print(sum)
if __name__ == "__main__":
    l = open("day1.input.txt").read().split("\n")
    main(l)