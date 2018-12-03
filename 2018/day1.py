def main(l):
    frequency = 0
    for i in l:
        frequency += int(i)
    print(frequency)

if __name__ == '__main__':
    l = open("day1.input.txt").read().split("\n")
    main(l)
