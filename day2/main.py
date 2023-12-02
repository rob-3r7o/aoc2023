target_reds = 12
target_greens = 13
target_blues = 14


def part_one(file):
    f = open(file, "r")

    result = 0
    id = 0

    for line in f:
        id += 1

        line = line.split(": ")[1]
        games = line.split("; ")

        for round in games:
            cubes = round.split(", ")

            for cube in cubes:
                num_color = cube.split()
                num_color[0] = num_color[0].strip()
                num_color[1] = num_color[1].strip()

                if num_color[1] == "red":
                    if int(num_color[0]) > target_reds:
                        break
                elif num_color[1] == "blue":
                    if int(num_color[0]) > target_blues:
                        break
                elif num_color[1] == "green":
                    if int(num_color[0]) > target_greens:
                        break

            else:
                continue

            break

        else:
            result += id

    print(result)


def part_two(file):
    f = open(file, "r")

    result = 0

    for line in f:
        line = line.split(": ")[1]
        games = line.split("; ")

        min_red = 0
        min_blue = 0
        min_green = 0

        for round in games:
            cubes = round.split(", ")

            for cube in cubes:
                num_color = cube.split()
                num_color[0] = num_color[0].strip()
                num_color[1] = num_color[1].strip()

                if num_color[1] == "red":
                    if int(num_color[0]) > min_red:
                        min_red = int(num_color[0])
                elif num_color[1] == "blue":
                    if int(num_color[0]) > min_blue:
                        min_blue = int(num_color[0])
                elif num_color[1] == "green":
                    if int(num_color[0]) > min_green:
                        min_green = int(num_color[0])

        result += min_red * min_blue * min_green

    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
