gears = {}


def part_one(file):
    f = open(file, "r").read().splitlines()

    result = 0
    number_done = False

    for i in range(len(f)):
        line = f[i]

        for j in range(len(line)):
            letter = line[j]

            if letter.isdigit():
                res = has_symbol_near(f, i, j)

                if res[0] and not number_done:
                    n = find_all_number(f, i, j)
                    result += n
                    number_done = True

                    if res[1]:
                        coord = res[2]

                        if coord in gears:
                            gears[coord].append(n)
                        else:
                            gears[coord] = [n]

            else:
                number_done = False

    print(result)


def has_symbol_near(file, line, letter):
    max_line = len(file) - 1
    max_letter = len(file[0]) - 1

    if line > 0:
        if letter > 0:
            if (not file[line - 1][letter - 1].isalnum()) and file[line - 1][
                letter - 1
            ] != ".":
                return [
                    True,
                    file[line - 1][letter - 1] == "*",
                    str(line - 1) + "-" + str(letter - 1),
                ]

        if (not file[line - 1][letter].isalnum()) and file[line - 1][letter] != ".":
            return [
                True,
                file[line - 1][letter] == "*",
                str(line - 1) + "-" + str(letter),
            ]

        if letter < max_letter:
            if (not file[line - 1][letter + 1].isalnum()) and file[line - 1][
                letter + 1
            ] != ".":
                return [
                    True,
                    file[line - 1][letter + 1] == "*",
                    str(line - 1) + "-" + str(letter + 1),
                ]

    if letter > 0:
        if (not file[line][letter - 1].isalnum()) and file[line][letter - 1] != ".":
            return [
                True,
                file[line][letter - 1] == "*",
                str(line) + "-" + str(letter - 1),
            ]
    if letter < max_letter:
        if (not file[line][letter + 1].isalnum()) and file[line][letter + 1] != ".":
            return [
                True,
                file[line][letter + 1] == "*",
                str(line) + "-" + str(letter + 1),
            ]

    if line < max_line:
        if letter > 0:
            if (not file[line + 1][letter - 1].isalnum()) and file[line + 1][
                letter - 1
            ] != ".":
                return [
                    True,
                    file[line + 1][letter - 1] == "*",
                    str(line + 1) + "-" + str(letter - 1),
                ]
        if (not file[line + 1][letter].isalnum()) and file[line + 1][letter] != ".":
            return [
                True,
                file[line + 1][letter] == "*",
                str(line + 1) + "-" + str(letter),
            ]
        if letter < max_letter:
            if (not file[line + 1][letter + 1].isalnum()) and file[line + 1][
                letter + 1
            ] != ".":
                return [
                    True,
                    file[line + 1][letter + 1] == "*",
                    str(line + 1) + "-" + str(letter + 1),
                ]

    return [False, False, ""]


def find_all_number(file, line, letter):
    max_letter = len(file[0]) - 1
    str_num = ""

    x = letter
    while x >= 0 and file[line][x].isdigit():
        str_num = str(file[line][x]) + str_num
        x -= 1

    x = letter + 1
    while x <= max_letter and file[line][x].isdigit():
        str_num = str_num + str(file[line][x])
        x += 1

    return int(str_num)


def part_two():
    result = 0

    for coord, values in gears.items():
        if len(values) > 1:
            result += values[0] * values[1]

    print(result)


part_one("data/data.txt")
part_two()
