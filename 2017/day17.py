def main(steps = 3, iterations = 2017):
    l = [0]
    pos = 0
    for i in range(0, iterations):
        pos = (pos + steps) % len(l)
        l.insert(pos + 1, i + 1)
        pos += 1
    print(l[l.index(2017) + 1])

if __name__ == '__main__':
    main(steps = 303)