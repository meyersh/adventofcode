#!/usr/bin/env python3

from tqdm import trange,tqdm
from collections import defaultdict,Counter

grid = defaultdict(lambda: defaultdict(lambda: '.'))

with open("inputs/day18.txt") as inputs:
    y = 0
    for row in inputs.readlines():
        row = row.rstrip()
        x = 0
        for c in row:
            grid[y][x] = c
            x += 1
        y += 1

def prettyprint():
    for y in range(0,51):
        for x in range(0,51):
            print(grid[y][x], end='')
        print()

def adjacencies(x,y):
    global grid
    c = Counter()
    for xi in range(x-1,x+2):
        for yi in range(y-1,y+2):
            if xi == x and yi == y: continue
            if grid[yi][xi] == '.': continue
            c[grid[yi][xi]] += 1
    return c



print(adjacencies(1,1))

def passMinute(size=50):
    global grid
    newgrid = defaultdict(lambda: defaultdict(lambda: '.'))

    def setgrid(x,y, c, newgrid=newgrid):
        """ ensure we're not planting outside the field. """
        if x >= 0 and x < size and y >= 0 and y < size:
            newgrid[y][x] = c

    for x in range(0,size):
        for y in range(0,size):
            adj = adjacencies(x,y)
            c = grid[y][x] # current

            ## | = Tree, # = Lumberyard, . = Empty.

            if c == '.' and adj['|'] >= 3:
                setgrid(x,y,'|')

            if c == '|':
                if adj['#'] >= 3:
                    setgrid(x,y,'#')
                else:
                    setgrid(x,y,c)

            if c == '#':
                if adj['#'] >= 1 and adj['|'] >= 1:
                    setgrid(x,y,'#')
                else:
                    setgrid(x,y,'.')

    return newgrid

def resources():
    global grid
    c = Counter()
    for x in range(0,50):
        for y in range(0,50):
            if grid[y][x] == '.': continue
            c[grid[y][x]] += 1

    return c

def computeResources():
    r = resources()
    return r['#'] * r['|']

#duration = 10*60 # 10 minutes.

## PART 1
#duration = 10
## PART 2
duration = 1000000000

n = 0
r = computeResources()
for minute in trange(0,duration):
    grid = passMinute(size=50)
    n += 1
    if n == 1000:
        tqdm.write("Minute = %6d, Resources=%d"%(minute+1, r))
        n = 0
        nr = computeResources()
        if nr == r:
            break
        r = nr



prettyprint()
rs = resources()
print("%s = %d" % (str(rs), rs['|']*rs['#']))
print()
assert rs['|']*rs['#'] >= 198950

# Part two (babY)
""" Analysis:
0 Minute =   2000, Resources=200364
1 Minute =   3000, Resources=198950
2 Minute =   4000, Resources=193965
3 Minute =   5000, Resources=188942
4 Minute =   6000, Resources=201026
5 Minute =   7000, Resources=193438
6 Minute =   8000, Resources=190162
0 Minute =   9000, Resources=200364
1 Minute =  10000, Resources=198950
2 Minute =  11000, Resources=193965
3 Minute =  12000, Resources=188942
4 Minute =  13000, Resources=201026
5 Minute =  14000, Resources=193438
6 Minute =  15000, Resources=190162
.
.
.
Minute = 998000, Resources=193965
Minute = 999000, Resources=188942
Minute = 1000000, Resources=201026
Minute = 1001000, Resources=193438
Minute = 1002000, Resources=190162
Minute = 1003000, Resources=200364
Minute = 1004000, Resources=198950
Minute = 1005000, Resources=193965

a = [200364, 198950, 193965, 188942, 201026, 193438, 190162]
def f(i): return (i//1000 - 2) % 7

NOT 190162...

"""
