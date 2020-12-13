def main(l):
    target = max(l) + 3
    l.insert(0, 0)
    l.append(target)
    difs = [l[i] - l[i - 1] for i in range(1, len(l))]
    print(difs.count(1) * difs.count(3))



if __name__ == "__main__":
    l = sorted([int(x) for x in open("day10.input.txt").read().split("\n")])
    main(l)
