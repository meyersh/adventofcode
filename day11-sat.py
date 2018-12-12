#!/usr/bin/env python3

# SUMMED AREA TABLE EDITION.  I like this. My implementation is
# currently off by one (that is, the answers are correct except that
# x,y are each one too small.

from pprint import pprint

gridserial = 7139 # the puzzle input.

def pl(x,y, gridserial=gridserial, verbose=False):
    rackid = x + 10
    powerlevel = y * rackid
    powerlevel += gridserial
    powerlevel *= rackid
    if verbose: print( "%d -> %d" % (powerlevel, (powerlevel//100)%10))
    powerlevel = (powerlevel//100)%10 # only the 100's
    powerlevel -= 5

    (((y * (x + 10) + gridserial ) * (x + 10))//100)%10 - 5
    
    return powerlevel

def squarelevel(x,y, size=3, gridserial=gridserial, verbose=False):
    """ given an x,y, check the square x,y thru x+2,y+2 and sum the
    power levels. """

    total = 0
    for xi in range(x,x+3):
        for yi in range(y,y+3):
            if verbose: print(xi,yi)
            total += pl(xi,yi,gridserial)

    return total

def maxpowercoord(squares):
    return max(squares, key=squares.get)

assert pl(122,79, 57) == -5
assert pl(217,196,39) == 0
assert pl(101,153,71) == 4

# Build a summed area table. x,y. Top left is 0,0. Bottom right = 301,301.
sat = dict()
running_sum = 0
for x in range(1,301):
    sat[x] = dict()
    for y in range(1,301):
        running_sum += pl(x,y)
        a = pl(x,y)
        try:
            b = sat[x][y-1]
        except:
            b = 0
        try:
            c = sat[x-1][y]
        except:
            c = 0

        try:
            d = sat[x-1][y-1]
        except:
            d=0
        sat[x][y] = a + b + c - d

def sat_squarelevel(x,y,size=3,gridserial=gridserial,verbose=False):
    # Where x,y is the TOP LEFT of the size x size square...

    # mine...
    return sat[x+size][y+size] + sat[x][y] - sat[x+size][y] - sat[x][y+size]
    # adjusted..
    #return sat[x][y] - sat[x][y-size] - sat[x-size][y] + sat[x-size][y-size]

# Part 1
print("Part 1.")
def findsquares(size=3):
    squares = dict()
    for x in range(size+1,300-size):
        for y in range(size+1,300-size):
            squares[(x,y)] = sat_squarelevel(x,y)
    return squares

squares = findsquares(size=3)
print( "Max: %s = %d" % (str(maxpowercoord(squares)),
                         squares[maxpowercoord(squares)]))

# Part 2
print("Part two party time... WITH SAT..?")
maxx = 0
maxy = 0
maxsize = 0
power = 0
for size in range(2, 300):
    for x in range(size+1,301-size):
        for y in range(size+1,301-size):
            mypower = sat_squarelevel(x,y,size,gridserial)
            if mypower > power:
                power = mypower
                maxx = x
                maxy = y
                maxsize = size

print("Max: (%d,%d,%d) = %d" % (
    maxx, maxy, maxsize, power))
