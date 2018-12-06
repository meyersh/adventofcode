#!/usr/bin/python

coords=list()
with open("inputs/day6.txt") as inputs:
    for line in inputs.readlines():
        line = line.rstrip()
                
        (x,y) = line.split(',')
        coords.append((int(x), int(y)))


coordss=set(coords)
## Find the boundaries of our points.
# x min, x max.
xbounds=(coords[0][0],coords[0][0])
# y min, y max.
ybounds=(coords[0][1],coords[0][1])
for (x,y) in coords:
    if x <= xbounds[0]:
        xbounds = (x - 1, xbounds[1])
    if x >= xbounds[1]:
        xbounds = (xbounds[0], x + 1)

    if y <= ybounds[0]:
        ybounds = (y - 1, ybounds[1])
    if y >= ybounds[1]:
        ybounds = (ybounds[0], y + 1)

print "Plane boundaries:"
print "X: ", xbounds
print "Y: ", ybounds

def d(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def nearestTo1(x,y):
    """ Nearest point to x,y. """
    closest = coords[0]
    for i in xrange(1, len(coords)):
        coord = coords[i]
        if d(coord, (x,y)) == d(closest, (x,y)):
            print "%s Equidistant: %s + %s" % (str((x,y)), str(coord), str(closest))
            return None
        if d(coord, (x,y)) < d(closest, (x,y)):
            closest = coord


    return closest

def nearestTo(x,y):
    ds = dict()
    for c in coords:
        ds[c] = d((x,y), c)

    distances = sorted(ds.values())
    if distances[0] == distances[1]:
        return None
    return min(ds, key=ds.get)

plane = dict()
areas = dict()
for xy in coords:
    areas[xy] = 1
    
for x in xrange(xbounds[0], xbounds[1]):
    plane[x] = dict()
    for y in xrange(ybounds[0], ybounds[1]):
        if (x,y) in coordss:
            plane[x][y] = (x,y) # Number it after the coordinate it belongs to...
        else: 
            plane[x][y] = nearestTo(x,y)
            # print "%s nearest %s." % ( str((x,y)), plane[x][y])

            if plane[x][y]: # we're not a shared coord, so this is the
                            # nearest point.
                areas[plane[x][y]] += 1 # increment the area since
                                        # we've found one unit..



# eliminate false "big" areas by skimming the borders of the plane.

# for x in xrange(xbounds[0], xbounds[1]):
#     for y in (ybounds[0], ybounds[1]-1):
#         if plane[x][y]:
#             if (x,y) in coordss:
#                 coordss.discard((x,y))
#                 del coords[coords.index((x,y))]
#                 print "Deleting ", str((x,y))

# for y in xrange(ybounds[0], ybounds[1]):
#     for x in (xbounds[0], xbounds[1]-1):
#         if plane[x][y]:
#             if (x,y) in coordss:
#                 coordss.discard((x,y))
#                 del coords[coords.index((x,y))]
#                 print "Deleting ", str((x,y))



biggest = None
area = 0
for xy in coords:
    # print "Checking %s." % str(xy)
    if areas[xy] > area:
        area = areas[xy]
        biggest = xy

print "Biggest area is owned by %s at %d units." % (str(biggest), area)
# NOT 2515
# NOT 4538 (too high)
# NOT 4771 (too high)

if False: # print the graph when true.
    for y in xrange(ybounds[0], ybounds[1]):
        for x in xrange(xbounds[0], xbounds[1]):
            if (x,y) in coordss:
                print 'X',
            elif plane[x][y]:
                print '.',
            elif plane[x][y] is None:
                print 'n',
            else:
                print " ",

        print ""
            

### PART B
muh_region = 0 # Area
dlimit = 10000
for x in xrange(xbounds[0], xbounds[1]):
    for y in xrange(ybounds[0], ybounds[1]):
        if sum(map(lambda c: d((x,y), c), coords)) < dlimit:
            muh_region += 1

print "The region under %d = %d." % (dlimit, muh_region)
