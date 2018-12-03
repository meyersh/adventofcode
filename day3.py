#!/usr/bin/python

# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........

# #123 @ 3,2: 5x4
# -> ID 123, 3" from left, 2" from top, 5 inches wide, 4 inches tall.



import re

claims = dict()
claimre = re.compile(r'#([0-9]+) @ (\d+),(\d+): (\d+)x(\d+)')
with open("inputs/day3.txt") as inputs:
    for claim in  [x.rstrip() for x in inputs.readlines()]:
        (claimid, leftmargin, topmargin, width, height) = claimre.match(claim).groups()
        claims[claimid] = {'leftmargin': int(leftmargin),
                           'topmargin':  int(topmargin),
                           'width': int(width),
                           'height': int(height)}
                           
furthestleft = 0
for c in claims:
    if int(claims[c]['leftmargin']) > furthestleft:
        furthestleft = int(claims[c]['leftmargin'])

print "furthest left = %d" % furthestleft

furthesttop = 0
for c in claims:
    if int(claims[c]['topmargin']) > furthesttop:
        furthesttop = int(claims[c]['topmargin'])

print "furthest top = %d" % furthesttop

claimed = dict()
for x in xrange(0,2000):
    claimed[x] = dict()
    for y in xrange(0,2000):
        claimed[x][y] = 0

print "allocated claims... now marking them in."

for claim in claims:
    leftmargin = claims[claim]['leftmargin']
    topmargin = claims[claim]['topmargin']
    height = claims[claim]['height']
    width = claims[claim]['width']
    for x in xrange(leftmargin, leftmargin+width):
        for y in xrange(topmargin, topmargin+height):
            claimed[x][y] += 1

squareinches = 0
for x in claimed:
    for y in claimed[x]:
        #print "(%d,%d) = %d " % (x,y, claimed[x][y])
        if claimed[x][y] >= 2:
            squareinches += 1

print "Detected %d in^2 over-claimed." % squareinches

for claim in claims:
    THEONE = True
    leftmargin = claims[claim]['leftmargin']
    topmargin = claims[claim]['topmargin']
    height = claims[claim]['height']
    width = claims[claim]['width']
    for x in xrange(leftmargin, leftmargin+width):
        if not THEONE:
            break
        for y in xrange(topmargin, topmargin+height):
            if claimed[x][y] != 1:
                THEONE = False
                break

    if THEONE:
        print "The one un-redundant claim is..."
        print claim
