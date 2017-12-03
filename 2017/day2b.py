from itertools import permutations

def get_divided_value(l):
    l = [int(x) for x in l]
    l = list(permutations(l, r=2))
    for i in l:
        print(i)
        if i[0] % i[1] == 0:
            return int(i[0] / i[1])

def main(s):
    checksum = 0
    l = [x.split("	") for x in s.split("\n")]
    for i in l:
        checksum += get_divided_value(i)
    print(checksum)

if __name__ == '__main__':
    s = open("day2.input.txt").read()
    main(s)