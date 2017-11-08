import re
def is_valid_triangle(triangle):
    return ((triangle[0] + triangle[1] > triangle[2]) and
            (triangle[1] + triangle[2] > triangle[0]) and
            (triangle[2] + triangle[0] > triangle[1]))

def main():
    with open("day3input.txt") as f:
        l_ = [k.split() for k in [j for j in [i for i in f.read().split("\n")]]]
    res = []
    for i in range(0, len(l_)-1, 3):
        for j in range(0, 3):
            if len(l_)-1 >= i+2:
                triangle = [int(l_[i][j]), int(l_[i+1][j]), int(l_[i+2][j])]
                if is_valid_triangle(triangle):
                    res.append(triangle)
    print(len(res))

if __name__ == '__main__':
    main()

#['883', '572', '842']
