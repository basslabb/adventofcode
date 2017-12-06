def main(l):
    pos = 0
    i = 0
    while pos < len(l) and pos >= 0:
        old_pos = pos
        value = l[pos] 
        pos += value
        offset = -1 if (pos - old_pos) >= 3 else 1
        l[old_pos] += offset
        i += 1
    print(i)

if __name__ == '__main__':
    l = [int(x) for x in open("day5.input.txt")]
    main(l)