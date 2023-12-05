import sys


def part_one(file):
    f = open(file, "r").read()  # .splitlines()

    nearest = sys.maxsize

    blocks = f.split("\n\n")
    seeds = blocks[0].split()[1:]
    maps = blocks[1:]

    for i in range(len(maps)):
        maps[i] = maps[i].strip().split("\n")[1:]

    # print("seeds:\n", seeds)
    # print("\nmaps:\n", maps)

    for seed in seeds:
        location = int(seed)
        # print("\n\t\tseed:", seed)
        for mp in maps:
            # print("\tmap:", mp)
            for row in mp:
                row = row.split()
                row = list(map(int, row))
                # start_range = list(range(row[1], row[1] + row[2]))
                # end_range = list(range(row[0], row[0] + row[2]))
                # print("start_range:", start_range)
                # print("end_range:", end_range)
                # if location in start_range:
                # print("\tlocation:", location)
                if location >= row[1] and location < row[1] + row[2]:
                    # print(
                    #     "ASSIGNING location to", end_range[start_range.index(location)]
                    # )
                    # location = end_range[start_range.index(location)]
                    # print("removing:", row[1] - row[0])
                    location = location - (row[1] - row[0])
                    break
            # print("location:", location)

        if location < nearest:
            nearest = location

    print(nearest)


part_one("data/data.txt")
# part_two("data/data.txt")
