def get_possibles_strings(s):
    return [s[i]+s[i+1]+s[i+2] for i in range(0, len(s)) if i+2 < len(s)]

def is_aba_string(s):
    return s[0] == s[2] and s[0] != s[1]

def supports_SSL(s):
    _supports_SSL = False
    in_brackets = [p.split(']')[0] for p in s.split('[') if ']' in p]
    outside_brackets = [p.split(']')[-1] for p in s.split('[')]
    pos_strings_in_brackets = [i for j in in_brackets for i in get_possibles_strings(j)]
    pos_strings_outside_brackets = [i for j in outside_brackets for i in get_possibles_strings(j)]
    for i in pos_strings_in_brackets:
        if is_aba_string(i) and i[1]+i[0]+i[1] in pos_strings_outside_brackets:
            _supports_SSL = True
            break
    return _supports_SSL

def main(l): 
    res = []
    for i in l:
        if supports_SSL(i):
            res.append(i)
    print(len(res))


if __name__ == '__main__':
    l = open("day7input.txt").read().split("\n")
    # l = ["abba[mnop]qrst"
    #     ,"abcd[bddb]xyyx"
    #     ,"aaaa[qwer]tyui"
    #     ,"ioxxoj[asdfgh]zxcvbn"]
    main(l)