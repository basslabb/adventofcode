
def main(l):
    for i in l:
        rest = [x for x in l if x != i]
        for j in rest:
            restrest = [x for x in rest if x != j]
            for k in restrest:
                if i + j + k == 2020:
                    print(i * j * k)
                    return
    
if __name__ == "__main__":
    l = [int(x) for x in open("day1.input.txt").read().split("\n")]
    #l = [1721,979,366,299,675,1456]
    main(l)