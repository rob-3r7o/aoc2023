y = 0
x = 1


def transpose_matrix(matrix):
    return [list(e) for e in (zip(*matrix))]


def expand_space(matrix, ret=False):
    new_matrix = []
    for i in range(len(matrix)):
        row = matrix[i]
        new_matrix.append(row)
        if len(list(filter(lambda x: x == ".", row))) == len(row):
            new_matrix.append(row)
    if ret:
        return new_matrix

    matrix = transpose_matrix(new_matrix)
    matrix = expand_space(matrix, True)
    return transpose_matrix(matrix)


def expand_space2(matrix, ret=False):
    rw_cl_to_expand = []
    for i in range(len(matrix)):
        row = matrix[i]
        if len(list(filter(lambda x: x == ".", row))) == len(row):
            rw_cl_to_expand.append(i)
    if ret:
        return rw_cl_to_expand

    matrix = transpose_matrix(matrix)

    return rw_cl_to_expand, expand_space2(matrix, True)


def part_one(file):
    f = open(file, "r").read()

    matrix = list(map(lambda row: list(row), f.splitlines()))

    result = 0
    galaxies = []

    # for row in matrix:
    #     print(row)
    matrix = expand_space(matrix)
    # for row in matrix:
    #     print(row)

    for yy in range(len(matrix)):
        for xx in range(len(matrix[0])):
            if matrix[yy][xx] == "#":
                galaxies.append((yy, xx))

    # print(galaxies)

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x_distance = galaxies[i][x] - galaxies[j][x]
            y_distance = galaxies[i][y] - galaxies[j][y]
            total_distance = abs(x_distance) + abs(y_distance)
            result += total_distance

    print(result)


def part_two(file):
    f = open(file, "r").read()

    matrix = list(map(lambda row: list(row), f.splitlines()))

    result = 0
    galaxies = []

    rows_to_expand, columns_to_expand = expand_space2(matrix)

    for yy in range(len(matrix)):
        for xx in range(len(matrix[0])):
            if matrix[yy][xx] == "#":
                galaxies.append((yy, xx))

    # print(galaxies)

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x_distance = galaxies[i][x] - galaxies[j][x]
            y_distance = galaxies[i][y] - galaxies[j][y]
            total_distance = abs(x_distance) + abs(y_distance)

            cntr = 1
            if galaxies[i][x] > galaxies[j][x]:
                cntr = -1

            common = list(
                set(list(range(galaxies[i][x], galaxies[j][x], cntr))).intersection(
                    columns_to_expand
                )
            )
            # print()
            # print("1 -", list(range(galaxies[i][x], galaxies[j][x], cntr)))
            # print("2 -", rows_to_expand)
            # print(common)

            if common:
                total_distance += expantion * len(common)

            cntr = 1
            if galaxies[i][y] > galaxies[j][y]:
                cntr = -1

            common = list(
                set((range(galaxies[i][y], galaxies[j][y], cntr))).intersection(
                    rows_to_expand
                )
            )
            # print("1 -", list(range(galaxies[i][y], galaxies[j][y], cntr)))
            # print("2 -", columns_to_expand)
            # print(common)

            if common:
                total_distance += expantion * len(common)

            result += total_distance

    print(result)


expantion = 1000000 - 1
part_one("data/data.txt")
part_two("data/data.txt")
