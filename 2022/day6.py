def main(s):
    for i in range(0, len(s)):
        if len(list(set(s[i:i+14]))) == 14:
            print(i+14)
            return


if __name__ == "__main__":
    #s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    #l = s.split("\n\n")
    s = open("day6.input.txt").read()
    main(s)
