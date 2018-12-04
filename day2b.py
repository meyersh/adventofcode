#!/usr/bin/python

with open("inputs/day2.txt") as inputs:
    data = [x.rstrip() for x in inputs.readlines()]

def dist(a,b):
    dist = len(a)
    for i in xrange(0,dist):
        if a[i] == b[i]:
            dist -= 1

    return dist

def matching(a,b):
    newstr = ""
    for i in xrange(0, len(a)):
        if a[i] == b[i]:
            newstr += a[i]

    return newstr

for i in xrange(0,len(data)):
    a = data[i]
    for j in xrange(i+1, len(data)):
        b = data[j]

        if i == j:
            continue
        
        if dist(a,b) < 2:
            print "%3d: %s" % (i, a)
            print "%3d: %s" % (j, b)

            print "---- %s" % matching(a,b)

