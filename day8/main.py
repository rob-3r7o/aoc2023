from math import lcm


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


# brute force (too slow)
def part_two(file):
    f = open(file, "r").read()

    directions, nodes = f.split("\n\n")

    directions = directions.replace("L", "0").replace("R", "1")

    starting_positions = []
    nodes_map = {}

    for line in nodes.strip().split("\n"):
        n1, n2_n3 = line.split(" = ")
        n2, n3 = n2_n3.replace("(", "").replace(")", "").split(", ")
        nodes_map[n1] = [n2, n3]
        if n1[-1] == "A":
            starting_positions.append(n1)

    current_nodes = starting_positions
    counter = 0

    while True:
        dir = int(directions[counter % len(directions)])
        for i in range(len(current_nodes)):
            current_nodes[i] = nodes_map[current_nodes[i]][dir]

        counter += 1

        if len(list(filter(lambda x: x.endswith("Z"), current_nodes))) == len(
            starting_positions
        ):
            break

    print(counter)


def part_two_better(file):
    f = open(file, "r").read()

    directions, nodes = f.split("\n\n")

    directions = directions.replace("L", "0").replace("R", "1")

    starting_positions = []
    nodes_map = {}

    for line in nodes.strip().split("\n"):
        n1, n2_n3 = line.split(" = ")
        n2, n3 = n2_n3.replace("(", "").replace(")", "").split(", ")
        nodes_map[n1] = [n2, n3]
        if n1[-1] == "A":
            starting_positions.append(n1)

    current_nodes = starting_positions
    counters = [0] * len(starting_positions)
    founds = [False] * len(starting_positions)
    counter = 0

    while True:
        dir = int(directions[counter % len(directions)])

        for i in range(len(current_nodes)):
            if not founds[i]:
                current_nodes[i] = nodes_map[current_nodes[i]][dir]
                counters[i] += 1

                if current_nodes[i][-1] == "Z":
                    founds[i] = True

        if len(list(filter(lambda x: x, founds))) == len(starting_positions):
            break

        counter += 1

    print(lcm(*counters))


part_one("data/data.txt")
part_two_better("data/data.txt")
