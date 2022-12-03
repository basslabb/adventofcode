from collections import Counter


def get_most_common_bit(l):
    if len(l) == 0:
        return []
    most_common_bits = []
    for i in range(0, len(l[0])):
        most_common_bits.append(Counter(([x[i] for x in l])).most_common())
    return most_common_bits


def get_oxygen_generator_rating(l, index=0):
    if len(l) == 1:
        return int("".join(l), 2)
    most_common_bit_for_index = get_most_common_bit(l)[index]
    if most_common_bit_for_index[0][1] == most_common_bit_for_index[1][1]:
        matching_bit_for_x = [x for x in l if x[index] == "1"]
    else:
        matching_bit_for_x = [x for x in l if x[index]
                              == most_common_bit_for_index[0][0]]
    return get_oxygen_generator_rating(matching_bit_for_x, index+1)


def get_scrubber_generator_rating(l, index=0):
    if len(l) == 1:
        return int("".join(l), 2)
    least_common_bit_for_index = get_most_common_bit(l)[index]
    if least_common_bit_for_index[0][1] == least_common_bit_for_index[1][1]:
        matching_bit_for_x = [x for x in l if x[index]
                              == "0"]
    else:
        matching_bit_for_x = [x for x in l if x[index]
                              == least_common_bit_for_index[1][0]]

    return get_scrubber_generator_rating(matching_bit_for_x, index+1)


def main(l):
    most_common_bits = []
    for i in range(0, len(l[0])):
        most_common_bits.append(Counter(([x[i] for x in l])).most_common())
    oxygen_generator_rating = get_oxygen_generator_rating(l)
    scrubber_generator_rating = get_scrubber_generator_rating(
        l)
    print(oxygen_generator_rating, scrubber_generator_rating)
    print(oxygen_generator_rating*scrubber_generator_rating)


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
