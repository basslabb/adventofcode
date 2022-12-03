from collections import Counter


def get_oxygen_generator_rating(l, most_common_bits):
    matching_first_bit = [x for x in l if x[0] == most_common_bits[0][0][0]]
    print(len(matching_first_bit))


def main(l):
    most_common_bits = []
    for i in range(0, len(l[0])):
        most_common_bits.append(Counter(([x[i] for x in l])).most_common())
    gamma_rate = int("".join([x[0][0] for x in most_common_bits]), 2)
    epsilon_rate = int("".join([x[1][0] for x in most_common_bits]), 2)
    print(gamma_rate*epsilon_rate)


if __name__ == "__main__":
    s = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    l = open("day3.input.txt").read().split("\n")
    #l = s.split("\n")

    main(l)
