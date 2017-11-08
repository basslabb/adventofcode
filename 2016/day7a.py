def is_abba_string(s):
    _is_abba_string = False
    l = [s[i]+s[i+1]+s[i+2]+s[i+3] for i in range(0, len(s)) if i+3 < len(s)]
    for i in l:
        if i[0] == i[3] and i[0] != i[1] and i[1] == i[2]:
            _is_abba_string = True
    return _is_abba_string

def supports_TLS(s):
    _supports_TLS = False
    in_brackets = [p.split(']')[0] for p in s.split('[') if ']' in p]
    outside_brackets = [p.split(']')[-1] for p in s.split('[')]
    for i in outside_brackets:
        if is_abba_string(i):
            _supports_TLS = True
            break
    for i in in_brackets:
        if is_abba_string(i):
            _supports_TLS = False
            break
    return _supports_TLS

def main(l):
    res = []
    for i in l:
        if supports_TLS(i):
            res.append(i)
    print(len(res))


if __name__ == '__main__':
    l = open("day7input.txt").read().split("\n")
    # l = ["abba[mnop]qrst"
    #     ,"abcd[bddb]xyyx"
    #     ,"aaaa[qwer]tyui"
    #     ,"ioxxoj[asdfgh]zxcvbn"]
    main(l)