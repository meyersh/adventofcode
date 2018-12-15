#!/usr/bin/python3


puzzle_input = "030121" # my input
#puzzle_input = "260321"

def part1(n, verbose=False):
    input = list("37")
    tick = 0
    e1 = 0   # index
    e2 = 1
    
    scores = [3,7]

    while len(input) <= 2+n+10:
        tick += 1
        if verbose:
            print ("t:{:5d} e1: {:d}, e2: {:d} -- {:s}".format(
                tick, int(input[e1]), int(input[e2]), " ".join(map(str,input[-15:]))))

        input += list(str(int(input[e1]) + int(input[e2])))
        e1 = (1 + e1 + int(input[e1])) % len(input)
        e2 = (1 + e2 + int(input[e2])) % len(input)


    return "".join(map(str,input[n:n+10]))

# The tests.
assert part1(5) == "0124515891"
assert part1(18) == "9251071085"
assert part1(2018) == "5941429882"

def part2(s, verbose=False):
    input = list("37")
    tick = 0
    e1 = 0   # index
    e2 = 1
    meh = 0
    searchbuf = len(s) + 1
    scores = [3,7]
    while s not in "".join(input[-searchbuf:]):
        tick += 1


        input += list(str(int(input[e1]) + int(input[e2])))
        e1 = (1 + e1 + int(input[e1])) % len(input)
        e2 = (1 + e2 + int(input[e2])) % len(input)


        meh += 1
        if meh == 10000 and verbose:
            meh = 0
            print ("t:{:5d} e1: {:d}, e2: {:d} -- {:s}".format(
                tick, int(input[e1]), int(input[e2]), "".join(map(str,input[-6:]))))


    return len(input)-len(s)

assert part2("01245") == 5
assert part2("51589") == 9
assert part2("92510") == 18
assert part2("594142") == 2018

print("Part1:")
print(part1(int(puzzle_input)))

print("Part2: {:d}".format(part2(puzzle_input, verbose=True)))
print(" subtract 1?")

