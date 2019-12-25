def interpret(M):
    for i in range(0, len(M)-1, 4):
        operator,pos1,pos2,index = M[i:i + 4]
        arg1 = M[pos1]
        arg2 = M[pos2]
        if operator == 1:
            M[index] = arg1 + arg2
        elif operator == 2:
            M[index] = arg1 * arg2
        elif operator == 99:
            break
    return M

def main(original):
    for noun in range(0, 100):
        for verb in range(0, 100):
            copy = [x for x in original]
            copy[1] = noun
            copy[2] = verb
            res = interpret(copy)
            if res[0] == 19690720:
                print(f'noun: {noun} verb: {verb}')
                print(f'res: {100 * noun + verb}')
                return
if __name__ == '__main__':
    l = [int(x) for x in open("day2.input.txt").read().split(",")]
    main(l)