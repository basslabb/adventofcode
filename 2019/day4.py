def main(min_value, max_value):
    valid_passwords = []
    for i in range(min_value, max_value):
        is_valid = has_adjacent_same_value(
            str(i)) and is_not_decreasing(str(i))
        if is_valid:
            valid_passwords.append(i)
    print(len(valid_passwords))


def has_adjacent_same_value(val):
    for i in range(len(val)):
        if i > 0 and val[i-1] == val[i]:
            return True
    return False


def is_not_decreasing(val):
    for i in range(len(val)):
        if i > 0 and val[i-1] > val[i]:
            return False
    return True


if __name__ == '__main__':
    #puzzle_input = "-767346"
    main(231832, 767346)
