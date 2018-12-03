def main(l):
    frequencys = {0}
    current_frequency = 0
    i = 0
    while True:
        value = l[i % len(l)]
        current_frequency += int(value)
        if current_frequency in frequencys:
            break
        frequencys.add(current_frequency)
        i+= 1
        
    print(current_frequency)


if __name__ == "__main__":
    l = open("day1.input.txt").read().split("\n")
    #l = ["+7", "+7", "-2", "-7", "-4"]
    main(l)