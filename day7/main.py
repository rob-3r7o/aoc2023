values1 = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}
values2 = {"A": "14", "K": "13", "Q": "12", "J": "01", "T": "10"}


def compare1(x):
    rank = 1
    tie_rank = "".join("0" + c if c.isdigit() else values1[c] for c in x[0])

    letters = {}

    for c in x[0]:
        letters[c] = letters.get(c, 0) + 1

    for k, v in letters.items():
        if v in [5, 4]:
            rank = v + 2
            break
        if v == 3:
            rank = 4
            for k1, v1 in letters.items():
                if k1 != k and v1 == 2:
                    rank = 5
                    break
            else:
                continue
            break
        if v == 2:
            rank = 2
            for k1, v1 in letters.items():
                if k1 != k and v1 == 2:
                    rank = 3
                    break

    return int(str(rank) + tie_rank)


def compare2(x):
    rank = 1
    tie_rank = "".join("0" + c if c.isdigit() else values2[c] for c in x[0])

    letters = {}

    for c in x[0]:
        letters[c] = letters.get(c, 0) + 1

    additional_points = letters["J"] if "J" in letters.keys() else 0

    for k, v in letters.items():
        if v == 5:
            rank = 7
            break
        if v == 4:
            rank = 6
            if k == "J" or additional_points > 0:
                rank = 7
            break
        if v == 3:
            rank = 4
            for k1, v1 in letters.items():
                if k1 != k and v1 == 2:
                    rank = 5
                    if k1 == "J" or k == "J":
                        rank = 7
                    break
            else:
                if additional_points > 0:
                    rank = 6
                continue
            break
        if v == 2:
            rank = 4 if additional_points > 0 else 2
            for k1, v1 in letters.items():
                if k1 != k and v1 == 2:
                    rank = 3
                    if k1 == "J" or k == "J":
                        rank = 6
                    elif additional_points > 0:
                        rank = 5
                    break

    if rank == 1:
        rank += additional_points

    return int(str(rank) + tie_rank)


def part_one(file):
    f = open(file, "r").read()

    lines = f.split("\n")
    hands = list(map(lambda x: x.split(), [ln for ln in lines]))[:-1]
    hands = [[a, int(b)] for a, b in hands]

    hands.sort(key=compare1)

    result = 0
    for i in range(len(hands)):
        result += hands[i][1] * (i + 1)
    print(result)


def part_two(file):
    f = open(file, "r").read()

    lines = f.split("\n")
    hands = list(map(lambda x: x.split(), [ln for ln in lines]))[:-1]
    hands = [[a, int(b)] for a, b in hands]

    hands.sort(key=compare2)

    result = 0
    for i in range(len(hands)):
        result += hands[i][1] * (i + 1)
    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
