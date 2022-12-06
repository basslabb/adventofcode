def main(s):
    for i in range(0, len(s)):
        if len(list(set(s[i:i+4]))) == 4:
            print(i+4)
            return


if __name__ == "__main__":
    #s = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    #l = s.split("\n\n")
    s = open("day6.input.txt").read()
    main(s)
