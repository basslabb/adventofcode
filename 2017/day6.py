from collections import Counter

def main(l):
    visited = []
    key = "".join([str(i) for i in l])
    while key not in visited:
        visited.append(key)
        _max, index = max(l), l.index(max(l))
        l[index] = 0
        while _max != 0:
            index += 1
            l[(index) % len(l)] += 1
            _max -= 1
        key = "".join([str(i) for i in l])
    print(len(visited))

if __name__ == '__main__':
    l = [int(i) for i in open("day6.input.txt").read().split("	")]
    main(l)