def main(l):
    pos = 0
    i = 0
    while pos < len(l) and pos >= 0:
        old_pos = pos
        value = l[pos] 
        pos += value
        l[old_pos] += 1
        i += 1
    print(i)


if __name__ == '__main__':
    l = [int(x) for x in open("day5.input.txt").read().split("\n")]
    #l = [0, 3, 0, 1, -3]
    main(l)