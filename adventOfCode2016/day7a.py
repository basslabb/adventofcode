import re
def has_repeating_characters(s):
    l = re.findall(r'(.+)(.+)\2\1', s)
    print(l, s)
    if len(l) == 0:
        return False
    for i in l:
        
        if i[0] != i[3] or i[1] != i[2] or i[0] == i[1] or i[2] == i[3]:
            return False
    return True
    #b = bool(re.search(r'([a-z])([a-z])\2\1', s))
    #return bool(re.search(r'([a-z])([a-z])\2\1', s))

def supports_TLs(s):
    in_brackets = re.findall(r"\[(.*?)\]", s)
    outside_brackets = re.findall(r'(.*?)\[.*?\]', s)
    for i in in_brackets:
        if has_repeating_characters(i):
            return False
    for i in outside_brackets:
        if has_repeating_characters(i):
            return True
    return False

def main(l):
    res = []
    for i in l:
        if supports_TLs(i):
            res.append(i)
    print(res)
    print(len(l), len(res))

if __name__ == '__main__':
    #l = open("day7input.txt").read().split("\n")
    l = ["abba[mnop]qrst",
        "abcd[bddb]xyyx",
        "aaaa[qwer]tyui",
        "ioxxoj[asdfgh]zxcvbn"]
    main(l)