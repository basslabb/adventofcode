from collections import defaultdict
def main(timestamp, buses):
    d = defaultdict(set)
    for i in range(1, timestamp + 1000):
        for bus in buses:
            if i % bus == 0:
                d[i].add(bus)
    next_bus = [(k,v) for k,v in d.items() if k > timestamp][0]
    print(next_bus)
    print((next_bus[0] - timestamp) * next_bus[1].pop())


if __name__ == "__main__":
    timestamp, bus_string = tuple(open("day13.input.txt").read().split("\n"))
    s = """939
7,13,x,x,59,x,31,19"""
    buses = [int(x) for x in bus_string.split(",") if x != "x"]
    main(int(timestamp), buses)