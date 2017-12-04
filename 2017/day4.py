from collections import Counter
def main(s):
    valid_passphrases = 0
    l = [x.split(" ") for x in s.split("\n")]
    for i in l:
        values = [v for v in Counter(i).values()]
        if all([v == 1 for v in values]):
            valid_passphrases += 1
    print(valid_passphrases)

if __name__ == '__main__':
    s = open("day4.input.txt").read()
    main(s)