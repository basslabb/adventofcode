

def main(l, preamble_index=25):
    for i in range(preamble_index, len(l)-1):
        previous = l[i-preamble_index:i]
        preamble_pairs = [(x, y) for x in previous for y in previous if x != y]
        matches = [(x, y) for x, y in preamble_pairs if x + y == l[i]]
        if len(matches) == 0:
            print(l[i])
            return


if __name__ == "__main__":
    l = [int(x) for x in open("day9.input.txt").read().split("\n")]
    main(l, 25)
