def get_symbols(s):
    d = {"register":"", "operation":"", "amount":0,  "condition":"", "a":"", "b":""}
    left, right = s.split("if ")
    left = [x.strip() for x in left.split(" ")]
    d["register"] = left[0]
    d["operation"] = left[1]
    d["amount"] = int(left[2])
    right = [x.strip() for x in right.split(" ")]
    d["a"] = right[0]
    d["condition"] = right[1]
    d["b"] = right[2]
    return d

def get_value(d, i):
    if i not in d:
        d[i] = 0
    return d[i]

def set_value(d,values, i, v, operation):
    if i not in d:
        d[i] = 0
    if operation == "inc":
        d[i] += v
    if operation == "dec":
        d[i] -= v
    values.append(d[i])

def parse_exp(a, condition, b):
    return "{0}{1}{2}".format(a, condition, b)

def main(l):
    d = {}
    values = []
    for line in l:
        symbols = get_symbols(line)
        a = get_value(d, symbols["a"])
        if eval(str(a) + symbols["condition"] + str(symbols["b"])):
            set_value(d, values,symbols["register"], symbols["amount"], symbols["operation"])
    print(sorted(values, reverse=True)[0])

if __name__ == '__main__':
    l = open("day8.input.txt").read().split("\n")
    main(l)