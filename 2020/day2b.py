from collections import Counter


def main(l):
    print(len([x for x in l if is_valid(*x)]))


def is_valid(num_tuple, character, password):
    val = [password[num_tuple[0]], password[num_tuple[1]]]
    return Counter(val)[character] == 1


def parse_input(s):
    policy, password = s.split(":")
    num_string, character = policy.split(" ")
    num_tuple = tuple([int(x) for x in num_string.split("-")])
    return (num_tuple, character, password)


if __name__ == "__main__":
    l = [parse_input(x) for x in open("day2.input.txt").read().split("\n")]
    # l = [parse_input(x)
    #      for x in ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]]
    main(l)
