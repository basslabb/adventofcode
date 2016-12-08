from hashlib import md5
def main(s):
    res = []
    i = 0
    while len(res) < 8:
        _s = (s+str(i)).encode("utf-8")
        h = md5(_s)
        if h.hexdigest().startswith("00000"):
            _h = h.hexdigest()[5:6]
            print(_h)
            res.append(_h)
            print(res)
        i += 1
    print("".join(res))

if __name__ == '__main__':
    #s = "abc"
    s = "reyedfim"
    main(s)