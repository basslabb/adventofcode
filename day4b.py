import collections
def is_valid_room(name, sector_id, check_sum):
    l = list("".join([i for i in name.split("-")]))
    counter = collections.Counter(l)
    counter = sorted(counter.most_common(len(counter)),
                     key=lambda element: (-element[1], element[0]))
    m = [i for j in counter for i in j[0]]
    for i in range(0, len(check_sum)):
        if check_sum[i] != m[i]:
            return False
    return True

def get_decrypted_value(s, sector_id):
    res = []
    s = [ord(i) for i in s]
    for i in range(0, sector_id):
        _s = []
        for c in s:
            c += 1
            if c == 123:
                c = 97
            if c in (46, 38, 33):
                c = 32
            _s.append(c)
        s = _s
    res = [chr(c) for c in s]
    return "".join(res)

def main(l):
    valid_rooms = []
    for i in l:
        _v, check_sum = i.split("[")
        check_sum = check_sum[:-1]
        name, sector_id = _v.rsplit("-", 1)
        sector_id = int(sector_id)
        if is_valid_room(name, sector_id, check_sum):
            decrypted_value = get_decrypted_value(name, sector_id)
            valid_rooms.append((decrypted_value, sector_id))
    northpole_object_storage = None
    for i in valid_rooms:
        if i[0] == "northpole object storage":
            northpole_object_storage = i
            break
    print(northpole_object_storage)
if __name__ == '__main__':
    l = open("day4input.txt").read().split("\n")
    #1514
    main(l)