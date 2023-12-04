def part_one(file):
    f = open(file, "r").read().splitlines()

    result = 0

    for i in range(len(f)):
        line = f[i]

        tmp = line.split("|")

        winning_n = tmp[0].split(":")[1].split()
        my_n = tmp[1]
        my_n = my_n.split()

        score = 0

        for n in my_n:
            # print(n, " in winning:")
            if n in winning_n:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        # print("\n\t", score)
        result += score

    print(result)


part_one("data/data.txt")
# part_two()
