def main(s):
    _sum = 0
    l = len(s)
    h = int(l/2)
    for i in range(0, l):
        i2 = (i + h) % l
        if s[i2] == s[i]:
            _sum += int(s[i])
    print(_sum)


if __name__ == '__main__':
    s = open("day1.input.txt").read()
    main(s)