import re


def main(l):
    required_fields = sorted(
        ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    valid_passports = 0
    for i in l:
        fields = [x for x in sorted(re.findall(r"(\w+):", i)) if x != "cid"]
        if required_fields == fields:
            valid_passports += 1
    print(valid_passports)


if __name__ == "__main__":
    l = [x.replace("\n", " ")
         for x in open("day4.input.txt").read().split("\n\n")]
    main(l)
