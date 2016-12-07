import collections
def is_valid_room(name, sector_id, check_sum):
    print(name, sector_id, check_sum)
    l = list("".join([i for i in name.split("-")]))
    counter = collections.Counter(l)
    counter = sorted(counter.most_common(len(counter)),
                     key=lambda element: (-element[1], element[0]))
    print(counter)
    m = [i for j in counter for i in j[0]]
    for i in range(0, len(check_sum)):
        print(counter, check_sum[i], m[i])
        if check_sum[i] != m[i]:
            return False
    return True

def main(l):
    print(l)
    res = []
    for i in l:
        _v, check_sum = i.split("[")
        check_sum = check_sum[:-1]
        name, sector_id = _v.rsplit("-", 1)
        sector_id = int(sector_id)
        if is_valid_room(name, sector_id, check_sum):
            print("Valid:", name, sector_id, check_sum)
            res.append(sector_id)
        else:
            print("Not Valid:", name, sector_id, check_sum)
    print(sum(res))
if __name__ == '__main__':
    l = open("day4input.txt").read().split("\n")
    #1514
    # l = ["aaaaa-bbb-z-y-x-123[abxyz]",
    #     "a-b-c-d-e-f-g-h-987[abcde]",
    #     "not-a-real-room-404[oarel]",
    #     "totally-real-room-200[decoy]"]
    main(l)