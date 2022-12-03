def main(l):
    depth_measurement_increase = 0
    last_measurement = None

    for i in range(3, len(l)+1):
        index = i-3
        current_measurement = sum(int(x) for x in l[index:index+3])
        if last_measurement == None:
            last_measurement = current_measurement
            continue
        if current_measurement > last_measurement:
            depth_measurement_increase += 1
        last_measurement = current_measurement

    print(depth_measurement_increase)


if __name__ == "__main__":
    s = """199
200
208
210
200
207
240
269
260
263"""
    l = open("day1.input.txt").read().split("\n")
    #l = s.split("\n")

    main(l)
