from functools import reduce
from operator import add
import time as tm


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
    f = open(file, "r").read().splitlines()

    time = int(reduce(add, f[0].split()[1:]))
    record = int(reduce(add, f[1].split()[1:]))

    # ---------- SOLUTION 1 (fastest)
    left_ptr = 0
    right_prt = time

    strt = tm.time()
    while True:
        left_ptr += 1
        if left_ptr * (time - left_ptr) > record:
            break

    while True:
        right_prt -= 1
        if right_prt * (time - right_prt) > record:
            break

    ways = right_prt - left_ptr + 1
    print(ways, "-", tm.time() - strt)

    # ---------- SOLUTION 2
    left_ptr = 1
    right_prt = time - 1
    left_done = False
    right_done = False

    strt = tm.time()
    while left_ptr < right_prt:
        if not left_done and left_ptr * (time - left_ptr) > record:
            left_done = True
        else:
            left_ptr += 1

        if not right_done and right_prt * (time - right_prt) > record:
            right_done = True
        else:
            right_prt -= 1

        if left_done and right_done:
            break

    ways = right_prt - left_ptr + 1
    print(ways, "-", tm.time() - strt)

    # ---------- SOLUTION 3 (slowest)
    strt = tm.time()
    ways = 0
    for btn_time in range(1, time):
        race_time = time - btn_time
        distace_traveled = btn_time * race_time

        if distace_traveled > record:
            ways += 1

    print(ways, "-", tm.time() - strt)


part_one("data/data.txt")
part_two("data/data.txt")
