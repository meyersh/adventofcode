#!/usr/bin/env python3

gridserial = 7139 # the puzzle input.

def pl(x,y, gridserial=gridserial, verbose=False):
    rackid = x + 10
    powerlevel = y * rackid
    powerlevel += gridserial
    powerlevel *= rackid
    if verbose: print( "%d -> %d" % (powerlevel, (powerlevel//100)%10))
    powerlevel = (powerlevel//100)%10 # only the 100's
    powerlevel -= 5

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

# Part 1
def findsquares(size=3):
    squares = dict()
    for x in range(0,300-size):
        for y in range(0,300-size):
            squares[(x,y)] = squarelevel(x,y)
    return squares

squares = findsquares()
print( "Max: %s = %d" % (str(maxpowercoord(squares)), squares[maxpowercoord(squares)]))

# Part 2

