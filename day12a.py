def get_value(s, d):
    LETTERS = "abcdefghijklmnopqrstuvwyxz"
    if s in LETTERS:
        return d[s]
    else:
        return int(s)

def main(l):    
    d = {"a":0,"b":0,"c":0,"d":0}
    i = 0
    while i < len(l):
        s = l[i].split(" ")
        if s[0] == "cpy":
            d[s[2]] = get_value(s[1], d)
        elif s[0] == "inc":
            d[s[1]] += 1
        elif s[0] == "dec":
            d[s[1]] -= 1
        elif s[0] == "jnz":
            val = get_value(s[1], d)
            if val != 0:
                i += int(s[2])
                continue
        i+=1
    print(d["a"])

if __name__ == '__main__':
    l = open("day12input.txt").read().split("\n")
    # l = ["cpy 41 a",
    #     "inc a",
    #     "inc a",
    #     "dec a",
    #     "jnz a 2",
    #     "dec a"]
    main(l)