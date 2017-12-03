def min_max(l):
    l = [int(x) for x in l]
    return (max(l), min(l))

def main(s):
    checksum = 0
    l = [x.split("	") for x in s.split("\n")]
    print(l)
    for i in l:
        t = min_max(i)
        checksum += t[0] -t[1]
    print(checksum)

if __name__ == '__main__':
    s = open("day2.input.txt").read()
    main(s)