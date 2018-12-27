#!/usr/bin/env python3

from day23 import d # get our distance func
from pprint import pprint

stars = list()
constellations = list()

with open("inputs/day25.txt") as input:
    for line in input.readlines():
        line = line.rstrip().split(',')
        points = tuple([int(x) for x in line])
        stars.append(points)

def partition():
    global constellations, stars

    while stars:
        cur_constellation = set()
        cur_constellation.add(stars.pop())
        nstars = 1 # cur_constellation.size()
        oldsize = 0
        while oldsize != nstars:
            oldsize = nstars
            for star in stars:
                newstars = set()
                for cstar in cur_constellation:
                    if d(star, cstar) <= 3:
                        newstars.add(star)
                        nstars += 1
                cur_constellation.update( newstars )
                
            for star in cur_constellation:
                try:
                    stars.remove(star)
                except ValueError: pass
        constellations.append(cur_constellation)

partition()
pprint(constellations)
print("That's %d constellations, total." % len(constellations))
