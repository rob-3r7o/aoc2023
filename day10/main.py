y = 0
x = 1


def part_one(file):
    f = open(file, "r").read()

    matrix = list(map(lambda row: list(row), f.splitlines()))

    steps = 0
    curr_pos = [0, 0]
    prev_pos = [0, 0]

    for yy in range(len(matrix)):
        for xx in range(len(matrix[y])):
            if matrix[yy][xx] == "S":
                curr_pos = prev_pos = [yy, xx]

    for yy in range(-1, 2, 1):
        for xx in range(-1, 2, 1):
            curr_char = matrix[curr_pos[y] + yy][curr_pos[x] + xx]
            checking_pos = [curr_pos[y] + yy, curr_pos[x] + xx]

            if curr_char in "|-LJ7F":
                match curr_char:
                    case "|":
                        if (
                            checking_pos[y] != curr_pos[y]
                            and checking_pos[x] == curr_pos[x]
                        ):
                            break
                    case "-":
                        if checking_pos[y] == curr_pos[y]:
                            break
                    case "L":
                        if (
                            checking_pos[y] == curr_pos[y]
                            and checking_pos[x] < curr_pos[x]
                        ):
                            break
                        if (
                            checking_pos[y] > curr_pos[y]
                            and checking_pos[x] == curr_pos[x]
                        ):
                            break
                    case "J":
                        if (
                            checking_pos[y] == curr_pos[y]
                            and checking_pos[x] > curr_pos[x]
                        ):
                            break
                        if (
                            checking_pos[y] > curr_pos[y]
                            and checking_pos[x] == curr_pos[x]
                        ):
                            break
                    case "7":
                        if (
                            checking_pos[y] == curr_pos[y]
                            and checking_pos[x] > curr_pos[x]
                        ):
                            break
                        if (
                            checking_pos[y] < curr_pos[y]
                            and checking_pos[x] == curr_pos[x]
                        ):
                            break
                    case "F":
                        if (
                            checking_pos[y] == curr_pos[y]
                            and checking_pos[x] < curr_pos[x]
                        ):
                            break
                        if (
                            checking_pos[y] < curr_pos[y]
                            and checking_pos[x] == curr_pos[x]
                        ):
                            break

        else:
            continue

        curr_pos = [curr_pos[y] + yy, curr_pos[x] + xx]
        break

    while True:
        steps += 1
        curr_char = matrix[curr_pos[0]][curr_pos[1]]
        curr_pos_copy = curr_pos.copy()

        match curr_char:
            case "|":
                if curr_pos[y] > prev_pos[y]:
                    curr_pos[y] += 1
                else:
                    curr_pos[y] -= 1
            case "-":
                if curr_pos[x] > prev_pos[x]:
                    curr_pos[x] += 1
                else:
                    curr_pos[x] -= 1
            case "L":
                if curr_pos[y] > prev_pos[y]:
                    curr_pos[x] += 1
                else:
                    curr_pos[y] -= 1
            case "J":
                if curr_pos[y] > prev_pos[y]:
                    curr_pos[x] -= 1
                else:
                    curr_pos[y] -= 1
            case "7":
                if curr_pos[y] < prev_pos[y]:
                    curr_pos[x] -= 1
                else:
                    curr_pos[y] += 1
            case "F":
                if curr_pos[y] < prev_pos[y]:
                    curr_pos[x] += 1
                else:
                    curr_pos[y] += 1
            case "S":
                break
            case ".":
                print("ERROR: REACHED GROUND")
                exit(1)

        prev_pos = curr_pos_copy

    print(steps // 2)


part_one("data/data.txt")
# part_two("data/data.txt")
