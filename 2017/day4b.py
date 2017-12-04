from collections import Counter

def main(s):
    valid_passphrases = 0
    l = [x for x in s.split("\n")]
    for i in l:
        count = sorted(list(Counter(["".join(sorted(x)) for x in i.split(" ")]).values()), reverse=True)
        if count[0] == 1:
            valid_passphrases += 1
    print(valid_passphrases)

if __name__ == '__main__':
    s = open("day4.input.txt").read()
    main(s)