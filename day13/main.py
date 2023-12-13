smudges = 0


def check_palindrome_horizontal(pattern):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            up = i - 1
            down = i + 2
            while up >= 0 and down < len(pattern) and pattern[up] == pattern[down]:
                up -= 1
                down += 1

            if up < 0 or down >= len(pattern) or pattern[up] == pattern[down]:
                return 100 * (i + 1)

    return check_palindrome_horizontal(transpose_matrix(pattern)) // 100


def check_palindrome_horizontal2(pattern):
    global smudges

    for i in range(len(pattern) - 1):
        smudges = 0
        if compare_patt(pattern[i], pattern[i + 1]):
            up = i - 1
            down = i + 2
            while (
                up >= 0
                and down < len(pattern)
                and compare_patt(pattern[up], pattern[down])
            ):
                up -= 1
                down += 1

            if (
                up < 0 or down >= len(pattern) or pattern[up] == pattern[down]
            ) and smudges != 0:
                return 100 * (i + 1)

    return check_palindrome_horizontal2(transpose_matrix(pattern)) // 100


def compare_patt(s1, s2):
    global smudges

    if s1 == s2:
        return True

    if smudges > 0:
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            smudges += 1
        if smudges > 1:
            return False

    return True


def transpose_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        line = ""
        for j in range(len(matrix)):
            line += matrix[j][i]
        new_matrix.append(line)
    return new_matrix


def part_one(file):
    f = open(file, "r").read()

    patterns = list(map(lambda line: line.split("\n"), f.strip().split("\n\n")))

    result = 0
    for pattern in patterns:
        result += check_palindrome_horizontal(pattern)

    print(result)


def part_two(file):
    f = open(file, "r").read()

    patterns = list(map(lambda line: line.split("\n"), f.strip().split("\n\n")))

    result = 0
    for pattern in patterns:
        result += check_palindrome_horizontal2(pattern)

    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
