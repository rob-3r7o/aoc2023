def part_one(file):
    f = open(file, "r").read().splitlines()

    times = list(map(int, f[0].split()[1:]))
    distances = list(map(int, f[1].split()[1:]))

    result = 1

    for i in range(len(times)):
        time = times[i]
        record = distances[i]

        ways = 0

        for btn_time in range(1, time):
            race_time = time - btn_time
            distace_traveled = btn_time * race_time

            if distace_traveled > record:
                ways += 1

        result *= ways

    print(result)


def part_two(file):
    None


part_one("data/data.txt")
# part_two("data/data.txt")
