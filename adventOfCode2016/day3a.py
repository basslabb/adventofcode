import re
def is_valid_triangle(triangle):
    print(triangle)
    triangle = [int(i) for i in triangle]
    print(triangle)
    return ((triangle[0] + triangle[1] > triangle[2]) and
            (triangle[1] + triangle[2] > triangle[0]) and
            (triangle[2] + triangle[0] > triangle[1]))

def main():
    l = []
    with open("day3input.txt") as f:
        _l = [re.findall(r'[0-9]+', i) for i in f.read().split("\n")]
    l = [i for i in _l if is_valid_triangle(i)]
    print(len(l))

if __name__ == '__main__':
    main()
