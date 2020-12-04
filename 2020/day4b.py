import re


def get_fields(i):
    field, value = i.split(":")
    if field == "hgt":
        matches = re.findall(r"([0-9]+)(cm|in)", value)
        tuple_value = tuple(matches)[0] if len(matches) > 0 else (0, "cm")
        return (field, tuple_value)
    return (field, value)


def main(l):
    valid_passports = 0
    validators = {
        "byr": lambda x: int(x) >= 1920 and int(x) <= 2002,
        "iyr": lambda x: int(x) >= 2010 and int(x) <= 2020,
        "eyr": lambda x: int(x) >= 2020 and int(x) <= 2030,
        "hgt": lambda x: True if (x[1] == "in" and int(x[0]) >= 59 and int(
            x[0]) <= 76) or (x[1] == "cm" and int(x[0]) >= 150 and int(x[0]) <= 193) else False,
        "hcl": lambda x: re.match('^#[a-f\d]{6}$', x) != None,
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: len(x) == 9 and x.isdigit(),
    }
    for i in l:
        fields = [get_fields(x) for x in re.split(
            '[\n ]', i) if x != ""]
        if len([x for x, y in fields if x != "cid"]) != len(validators.keys()):
            continue
        is_valid = list(set([(validators[x](y))
                             for x, y in fields if x in validators]))

        if len(is_valid) == 1 and is_valid[0]:
            valid_passports += 1
    print(valid_passports)


if __name__ == "__main__":
    l = [x.replace("\n", " ")
         for x in open("day4.input.txt").read().split("\n\n")]
    main(l)
