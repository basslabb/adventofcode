import collections
def main(l):
    _l = []
    res = []
    for i in range(0, 8):
        col = []
        for j in range(0, len(l)):
            col.append(l[j][i:i+1])
        _l.append(col)
    print(_l[5])
    for i in _l:
        most_common = collections.Counter(i).most_common(28)
        print([i[0] for i in most_common])
        res.append(most_common[0][0])
    print("".join(res))

if __name__ == '__main__':
    l = open("day6input.txt").read().split("\n")
    # l = ["eedadn",
    # "drvtee",
    # "eandsr",
    # "raavrd",
    # "atevrs",
    # "tsrnev",
    # "sdttsa",
    # "rasrtv",
    # "nssdts",
    # "ntnada",
    # "svetve",
    # "tesnvt",
    # "vntsnd",
    # "vrdear",
    # "dvrsen",
    # "enarar"]
    main(l)