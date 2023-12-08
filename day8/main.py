import time


def part_one(file):
    f = open(file, "r").read()

    directions, nodes = f.split("\n\n")
    directions = directions.replace("L", "0").replace("R", "1")

    nodes_map = {}

    for line in nodes.strip().split("\n"):
        n1, n2_n3 = line.split(" = ")
        n2, n3 = n2_n3.replace("(", "").replace(")", "").split(", ")
        nodes_map[n1] = [n2, n3]

    current_node = "AAA"
    counter = 0

    while current_node != "ZZZ":
        dir = int(directions[counter % len(directions)])
        current_node = nodes_map[current_node][dir]
        counter += 1

    print(counter)


counter = 0


def part_two(file):
    f = open(file, "r").read()

    directions, nodes = f.split("\n\n")

    directions = directions.replace("L", "0").replace("R", "1")
    print(directions)

    starting_positions = []
    nodes_map = {}

    for line in nodes.strip().split("\n"):
        print(line)
        n1, n2_n3 = line.split(" = ")
        n2, n3 = n2_n3.replace("(", "").replace(")", "").split(", ")
        nodes_map[n1] = [n2, n3]
        if n1[-1] == "A":
            starting_positions.append(n1)

    current_nodes = starting_positions
    print(current_nodes)
    # n_of_starting = len(starting_positions)
    global counter

    while True:
        # time.sleep(0.2)
        # print()
        # print("current:", current_nodes)
        dir = int(directions[counter % len(directions)])
        for i in range(len(current_nodes)):
            current_nodes[i] = nodes_map[current_nodes[i]][dir]
            # print("HERE counter->", counter)
            # n_of_starting -= 1
            # print("HERE n_of_starting->", n_of_starting)
        counter += 1
        if len(list(filter(lambda x: x.endswith("Z"), current_nodes))) == len(
            starting_positions
        ):
            break
        # print("direction:", dir)
        # print("going to:", current_nodes)
        if counter % 10000000 == 0:
            print(11795205644011)
            print(counter)

    print(counter)


try:
    part_one("data/data.txt")
    # part_two("data/data.txt")
except KeyboardInterrupt:
    print(counter)
    exit(0)

    # import math
    #
    # M, *I = open("data/data.txt")
    # S = {l[:3]: l[7:].split() for l in I}
    # for s in 3, 1:
    #     print(
    #         math.lcm(
    #             *[
    #                 len(
    #                     [
    #                         p := S[p][m > "L"][:3]
    #                         for m in M[:-1] * 99
    #                         if "Z" * s > p[-s:]
    #                     ]
    #                 )
    #                 for q in S
    #                 if "A" * s == (p := q)[-s:]
    #             ]
    #         )
    #     )
