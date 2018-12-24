#!/usr/bin/env python3

from pprint import pprint
from tqdm import trange

import re
nanobotre = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")

nanobots = dict()

minbound = [0,0,0]
maxbound = [0,0,0]
with open("inputs/day23.txt") as input:
    for line in input.readlines():
        match = nanobotre.match(line.rstrip())
        if match:
            (x,y,z,r) = match.groups()
            x = int(x)
            y = int(y)
            z = int(z)
            r = int(r)
            nanobots[(x,y,z)] = r
            for coord in range(0,3):
                if (x,y,z)[coord] > maxbound[coord]:
                    maxbound[coord] = (x,y,z)[coord]
                if (x,y,z)[coord] < minbound[coord]:
                    minbound[coord] = (x,y,z)[coord]
                

print("Space edges: %s to %s." % (str(minbound), str(maxbound)))

def biggest():
    global nanobots
    mymax = 0
    bigboi = None
    for nb in nanobots:
        if nanobots[nb] > mymax:
            mymax = nanobots[nb]
            bigboi = nb
            
    return bigboi

def d(a,b):
    return sum(map(
        lambda elem:abs(elem[0]-elem[1]),
        zip(a,b)))

def inrange(a):
    
    global nanobots
    inrange = list()
    for nb in nanobots:

        if d(a, nb) <= nanobots[a]:
            inrange.append(nb)

    return inrange

def maxinrange():
    global nanobots
    bestcoord = (0,0,0)
    bestn = 0
    for x in trange(minbound[0], maxbound[0]+1, desc="X coords"):
        for y in trange(minbound[1], maxbound[1]+1, desc="Y coords"):
            for z in trange(minbound[2], maxbound[2]+1, desc="Z coords"):
                inr = 0
                for nb in nanobots:
                    if d((x,y,z), nb) <= nanobots[nb]:
                        inr += 1
                if inr > bestn:
                    bestn = inr
                    bestcoord = (x,y,z)

    return bestcoord
                
#pprint(nanobots)

thebiggest = biggest()
print("Biggest nanobot at %s, r=%d." % (str(thebiggest), nanobots[thebiggest]))
inr = inrange(thebiggest)
#pprint(inrange(thebiggest))
print("%d of them in range." % len(inr))

#assert len(inr) > 262
bestcoord = maxinrange()
print("Best coord: %s @ d=%d" % (str(bestcoord), d((0,0,0), bestcoord)))
