import time
import os


def dynamic_print(matrix):
    os.system("clear")
    print("\n\n")
    print("\n".join("".join(line) for line in matrix))
    time.sleep(0.2)


def move_up(y, x, matrix):
    value = len(matrix) - y
    for yy in range(y - 1, -1, -1):
        if matrix[yy][x] == ".":
            matrix[yy][x] = "O"
            matrix[yy + 1][x] = "."
            value = len(matrix) - yy
        else:
            break

    return value


def move_north(y, x, matrix):
    if y <= 0:
        return y

    new_y = y
    for yy in range(y - 1, -1, -1):
        if matrix[yy][x] == ".":
            matrix[yy][x] = "O"
            matrix[yy + 1][x] = "."
            new_y = yy

        else:
            break

    return new_y


def move_west(y, x, matrix):
    if x <= 0:
        return x

    new_x = x
    for xx in range(x - 1, -1, -1):
        if matrix[y][xx] == ".":
            matrix[y][xx] = "O"
            matrix[y][xx + 1] = "."
            new_x = xx

        else:
            break

    return new_x


def move_south(y, x, matrix):
    if y >= len(matrix) - 1:
        return y

    new_y = y
    for yy in range(y + 1, len(matrix), 1):
        if matrix[yy][x] == ".":
            matrix[yy][x] = "O"
            matrix[yy - 1][x] = "."
            new_y = yy

        else:
            break

    return new_y


def move_east(y, x, matrix):
    if x >= len(matrix[0]) - 1:
        return x

    new_x = x
    for xx in range(x + 1, len(matrix[0]), 1):
        if matrix[y][xx] == ".":
            matrix[y][xx] = "O"
            matrix[y][xx - 1] = "."
            new_x = xx

        else:
            break

    return new_x


def part_one(file):
    f = open(file, "r").read()

    matrix = list(map(lambda line: list(line), f.splitlines()))

    load = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if matrix[y][x] == "O":
                load += move_up(y, x, matrix)

    print(load)


# Brute force solution :(
# Actually cycling 1000 times is the same as 1000000000
def part_two(file):
    f = open(file, "r").read()

    matrix = list(map(lambda line: list(line), f.splitlines()))

    load = 0
    # cycles = 1000000000
    cycles = 1000

    for i in range(cycles):
        for x in range(len(matrix[0])):
            for y in range(len(matrix)):
                if matrix[y][x] == "O":
                    move_north(y, x, matrix)
                    # dynamic_print(matrix)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == "O":
                    move_west(y, x, matrix)
                    # dynamic_print(matrix)
        for x in range(len(matrix[0])):
            for y in range(len(matrix) - 1, -1, -1):
                if matrix[y][x] == "O":
                    move_south(y, x, matrix)
                    # dynamic_print(matrix)
        for y in range(len(matrix)):
            for x in range(len(matrix[0]) - 1, -1, -1):
                if matrix[y][x] == "O":
                    move_east(y, x, matrix)
                    # dynamic_print(matrix)

    for i in range(len(matrix)):
        load += matrix[i].count("O") * (len(matrix) - i)

    print(load)


part_one("data/data.txt")
part_two("data/data.txt")
