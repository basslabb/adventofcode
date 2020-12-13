def main(l):
    target = max(l) + 3
    l.append(target)
    a = {0: 1}
    for i in l:
        a[i] = a.get(i - 1, 0) + a.get(i - 2, 0) + a.get(i - 3, 0)
    print(a[-1])
    



if __name__ == "__main__":
    l = sorted([int(x) for x in open("day10.input.txt").read().split("\n")])
    main(l)
