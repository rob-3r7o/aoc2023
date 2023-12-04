def part_one(file):
    f = open(file, "r").read().splitlines()

    result = 0

    for i in range(len(f)):
        line = f[i]

        tmp = line.split("|")

        winning_n = tmp[0].split(":")[1].split()
        my_n = tmp[1]
        my_n = my_n.split()

        score = 0

        for n in my_n:
            if n in winning_n:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        result += score

    print(result)


def part_two(file):
    f = open(file, "r").read().splitlines()

    result = 0
    copies_counter = {}

    for i in range(len(f)):
        line = f[i]

        tmp = line.split("|")

        id = int(tmp[0].split(":")[0].split()[1])
        winning_n = tmp[0].split(":")[1].split()
        my_n = tmp[1].split()

        repeater = 1
        score = 0

        for n in my_n:
            if n in winning_n:
                score += 1

        if id in copies_counter:
            copies_counter[id] += 1
            repeater = copies_counter[id]
        else:
            copies_counter[id] = 1

        for i in range(id + 1, id + 1 + score):
            if i in copies_counter:
                copies_counter[i] += repeater
            else:
                copies_counter[i] = repeater

    for _, copies in copies_counter.items():
        result += copies

    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
