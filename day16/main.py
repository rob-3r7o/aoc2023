import os
import time

seen_pos = {}


def dynamic_print(matrix):
    os.system("clear")
    print("\n\n")
    print("\n".join("".join(line) for line in matrix))
    time.sleep(0.2)


def go_right(y, x, grid):
    while x < len(grid[0]) and grid[y][x] in ".-#":
        if (y, x, "r") in seen_pos:
            seen_pos[(y, x, "r")] += 1
            return
        else:
            seen_pos[(y, x, "r")] = 1
        if grid[y][x] == ".":
            grid[y][x] = "#"
        x += 1
        # dynamic_print(grid)

    if x >= len(grid[0]):
        return

    if (y, x, "r") in seen_pos:
        seen_pos[(y, x, "r")] += 1
        return
    else:
        seen_pos[(y, x, "r")] = 1

    if grid[y][x] in "/|":
        go_up(y - 1, x, grid)
    if grid[y][x] in "\\|":
        go_down(y + 1, x, grid)


def go_left(y, x, grid):
    while x >= 0 and grid[y][x] in ".-#":
        if (y, x, "l") in seen_pos:
            seen_pos[(y, x, "l")] += 1
            return
        else:
            seen_pos[(y, x, "l")] = 1
        if grid[y][x] == ".":
            grid[y][x] = "#"
        x -= 1
        # dynamic_print(grid)

    if x < 0:
        return

    if (y, x, "l") in seen_pos:
        seen_pos[(y, x, "l")] += 1
        return
    else:
        seen_pos[(y, x, "l")] = 1

    if grid[y][x] in "/|":
        go_down(y + 1, x, grid)
    if grid[y][x] in "\\|":
        go_up(y - 1, x, grid)


def go_up(y, x, grid):
    while y >= 0 and grid[y][x] in ".|#":
        if (y, x, "u") in seen_pos:
            seen_pos[(y, x, "u")] += 1
            return
        else:
            seen_pos[(y, x, "u")] = 1
        if grid[y][x] == ".":
            grid[y][x] = "#"
        y -= 1
        # dynamic_print(grid)

    if y < 0:
        return

    if (y, x, "u") in seen_pos:
        seen_pos[(y, x, "u")] += 1
        return
    else:
        seen_pos[(y, x, "u")] = 1

    if grid[y][x] in "/-":
        go_right(y, x + 1, grid)
    if grid[y][x] in "\\-":
        go_left(y, x - 1, grid)


def go_down(y, x, grid):
    while y < len(grid) and grid[y][x] in ".|#":
        if (y, x, "d") in seen_pos:
            seen_pos[(y, x, "d")] += 1
            return
        else:
            seen_pos[(y, x, "d")] = 1
        if grid[y][x] == ".":
            grid[y][x] = "#"
        y += 1
        # dynamic_print(grid)

    if y >= len(grid):
        return

    if (y, x, "d") in seen_pos:
        seen_pos[(y, x, "d")] += 1
        return
    else:
        seen_pos[(y, x, "d")] = 1

    if grid[y][x] in "/-":
        go_left(y, x - 1, grid)
    if grid[y][x] in "\\-":
        go_right(y, x + 1, grid)


def part_one(file):
    f = open(file, "r").read().splitlines()
    grid = list(map(lambda line: list(line), f))

    go_right(0, 0, grid)

    new_seen_pos = {}
    for k, v in seen_pos.items():
        new_seen_pos[(k[0], k[1])] = 1

    print(len(new_seen_pos))


def part_two(file):
    global seen_pos
    f = open(file, "r").read().splitlines()
    grid = list(map(lambda line: list(line), f))
    max = 0

    # ---
    for i in range(len(grid[0])):
        seen_pos = {}
        go_down(0, i, grid)

        new_seen_pos = {}
        for k, v in seen_pos.items():
            new_seen_pos[(k[0], k[1])] = 1
        if len(new_seen_pos) > max:
            max = len(new_seen_pos)

    # ---
    for i in range(len(grid)):
        seen_pos = {}
        go_right(i, 0, grid)

        new_seen_pos = {}
        for k, v in seen_pos.items():
            new_seen_pos[(k[0], k[1])] = 1
        if len(new_seen_pos) > max:
            max = len(new_seen_pos)

    # ---
    for i in range(len(grid[0])):
        seen_pos = {}
        go_up(len(grid) - 1, i, grid)

        new_seen_pos = {}
        for k, v in seen_pos.items():
            new_seen_pos[(k[0], k[1])] = 1
        if len(new_seen_pos) > max:
            max = len(new_seen_pos)

    # ---
    for i in range(len(grid)):
        seen_pos = {}
        go_left(len(grid) - 1, i, grid)

        new_seen_pos = {}
        for k, v in seen_pos.items():
            new_seen_pos[(k[0], k[1])] = 1
        if len(new_seen_pos) > max:
            max = len(new_seen_pos)

    print(max)


part_one("data/data.txt")
part_two("data/data.txt")
