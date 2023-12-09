def part_one(file):
    f = open(file, "r").read()

    rows = f.splitlines()
    result = 0

    for row in rows:
        differences = [list(map(int, row.split()))]
        counter = 0

        while True:
            diff = []
            for i in range(len(differences[counter]) - 1):
                diff.append(differences[counter][i + 1] - differences[counter][i])

            differences.append(diff)
            counter += 1

            if len(list(filter(lambda x: x == 0, diff))) == len(diff):
                break

        for i in range(len(differences) - 2, -1, -1):
            differences[i].append(differences[i][-1] + differences[i + 1][-1])

        result += differences[0][-1]

    print(result)


def part_two(file):
    f = open(file, "r").read()

    rows = f.splitlines()
    result = 0

    for row in rows:
        differences = [list(map(int, row.split()))]
        counter = 0

        while True:
            diff = []
            for i in range(len(differences[counter]) - 1):
                diff.append(differences[counter][i + 1] - differences[counter][i])

            differences.append(diff)
            counter += 1

            if len(list(filter(lambda x: x == 0, diff))) == len(diff):
                break

        for i in range(len(differences) - 2, -1, -1):
            differences[i].insert(0, differences[i][0] - differences[i + 1][0])

        result += differences[0][0]

    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
