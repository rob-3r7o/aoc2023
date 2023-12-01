def part_one():
    f = open("data/data.txt", "r")

    result = 0

    for line in f:
        first = -1
        last = -1

        for letter in line:
            try:
                if first == -1:
                    first = last = int(letter)
                else:
                    last = int(letter)
            except:
                continue

        result += int(str(first) + str(last))

    print(result)


def part_two():
    f = open("data/data.txt", "r")

    numbers_dic = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    result = 0

    for line in f:
        first = -1
        last = -1

        for i, j in numbers_dic.items():
            line = line.replace(i, j)

        for letter in line:
            try:
                if first == -1:
                    first = int(letter)
                else:
                    last = int(letter)

            except:
                continue

        if last != -1:
            result += int(str(first) + str(last))
        else:
            result += int(str(first) + str(first))

    print(result)


part_one()
part_two()
