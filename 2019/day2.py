def foo(l, pos=0):
    if l[pos] == 99:
        return l
    operator,pos1,pos2,index = l[pos:pos + 4]
    arg1 = l[pos1]
    arg2 = l[pos2]
    if operator == 1:
        l[index] = arg1 + arg2
    if operator == 2:
        l[index] = arg1 * arg2
    pos += 4
    return foo(l, pos)

def main(l):
    l[1] = 12
    l[2] = 2
    res = foo(l)
    print(res[0])
    
if __name__ == '__main__':
    l = [int(x) for x in open("day2.input.txt").read().split(",")]
    main(l)