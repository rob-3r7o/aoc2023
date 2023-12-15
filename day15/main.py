def get_hash_result(s):
    result = 0

    for c in s:
        result += ord(c)
        result *= 17
        result %= 256

    return result


def part_one(file):
    f = open(file, "r").read().strip().split(",")

    sum = 0

    for step in f:
        sum += get_hash_result(step)

    print(sum)


def part_two(file):
    f = open(file, "r").read().strip().split(",")

    sum = 0
    boxes = {}

    for step in f:
        if "=" in step:
            label = step.split("=")[0]
            sign = "="
            focal_l = int(step[-1])
        else:
            label = step[:-1]
            sign = "-"
            focal_l = -1
        hash = get_hash_result(label)

        if sign == "=":
            boxes[label] = [focal_l, hash]
        else:
            boxes.pop(label, None)

    positions = {}

    for k, v in boxes.items():
        if v[1] not in positions:
            positions[v[1]] = 1
        else:
            positions[v[1]] += 1

        sum += (v[1] + 1) * positions[v[1]] * v[0]

    print(sum)


part_one("data/data.txt")
part_two("data/data.txt")
