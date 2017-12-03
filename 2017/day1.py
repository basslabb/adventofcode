def main(s):
    print(s)
    _sum = 0
    for i in range(0, len(s)):
        i2 = 0 if i == len(s)-1 else i+1
        if s[i2] == s[i]:
            _sum += int(s[i])
    print(_sum)


if __name__ == '__main__':
    s = open("day1a.input.txt").read()
    main(s)