
def get_invalid_number(l, preamble_index=25):
    for i in range(preamble_index, len(l)-1):
        previous = l[i-preamble_index:i]
        preamble_pairs = [(x, y) for x in previous for y in previous if x != y]
        matches = [(x, y) for x, y in preamble_pairs if x + y == l[i]]
        if len(matches) == 0:
            return l[i]


def main(l, preamble_index=25):
    invalid_number = get_invalid_number(l, preamble_index)
    print(invalid_number)
    for i in range(0, len(l) - 1):
        sequence = [l[i]]
        for j in range(i+1, len(l) - 1):
            sequence.append(l[j])
            if sum(sequence) > invalid_number:
                break
            if sum(sequence) == invalid_number:
                print(min(sequence) + max(sequence))
                return


if __name__ == "__main__":
    l = [int(x) for x in open("day9.input.txt").read().split("\n")]
    main(l, 25)
