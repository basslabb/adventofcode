from hashlib import md5
def is_valid_password(l):
    for i in l:
        if i == None:
            return False
    return True

def main(s):
    res = [None for i in range(0,8)]
    i = 0
    while is_valid_password(res) == False:
        _s = (s+str(i)).encode("utf-8")
        h = md5(_s)
        if h.hexdigest().startswith("00000"):
            pos, val  = h.hexdigest()[5:6], h.hexdigest()[6:7]
            if pos.isdigit():
                pos = int(pos)
                print(res[pos:pos+1])
                if pos < len(res) and res[pos:pos+1] is None:
                    print(res, pos, val)
                    res[pos:pos+1] = val
        i += 1
    print("".join(res))


if __name__ == '__main__':
    s = "abc"
    #s = "reyedfim"
    main(s)