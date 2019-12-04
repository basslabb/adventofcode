import math

def get_fuel(fuel, sum=0):
    new_fuel = math.floor(fuel / 3) - 2
    if new_fuel <= 0:
        return sum
    sum += new_fuel
    return get_fuel(new_fuel, sum)

def main(l):
    sum = 0
    for i in l:
        sum += get_fuel(int(i))
    print(sum)

if __name__ == "__main__":
    l = open('day1.input.txt').read().split('\n')
    main(l)