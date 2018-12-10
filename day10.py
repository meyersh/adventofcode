#!/usr/bin/python
# Requires wx, I just used `brew install wxpython`.

import re
parsere = re.compile("position=<(.*), (.*)> velocity=<(.*), +(.*)>")

from pprint import pprint

import time

class Node(object):
    def __init__(self, x, y, velx, vely):
        self.x = int(x)
        self.y = int(y)

        self.velx = int(velx)
        self.vely = int(vely)

    def __repr__(self):
        return "<(%d+%d,%d+%d)>" % (
            self.x, self.velx,
            self.y, self.vely)

    def advanceTime(self, t=1):
        self.x += t * self.velx
        self.y += t * self.vely


nodes = list()

with open("inputs/day10.txt") as input:
    for line in input.readlines():
        (x, y, velx, vely) = parsere.match(line.rstrip()).groups()
        nodes.append(Node(x,y,velx,vely))


def bounds(nodes=nodes):
    a = sorted(nodes)
    return (a[0].x, a[0].y), (a[-1].x, a[-1].y)


def area(b):
    """ given a bounds obj, what's the area (x*y) ? """
    return abs(b[0][0]-b[1][0]) * abs(b[0][1]-b[1][1])


def lineyness(nodes = nodes):
    xs = dict()
    ys = dict()
    for node in nodes:
        if node.x not in xs:
            xs[node.x] = 0

        if node.y not in ys:
            ys[node.y] = 0

        xs[node.x] += 1
        ys[node.y] += 1

    return max(xs.values()) * max(ys.values())
pprint(nodes)

print bounds()

from matplotlib import pyplot as plt

t=0

liney = list()
areas = list()

def showme(nodes=nodes):
    for node in nodes:
        plt.plot(node.x, -node.y, "ob")

    plt.show()

while t < 20000:
    a = area(bounds())
    aa = bounds()
    al = lineyness()
    for node in nodes:
        node.advanceTime(1)

    liney.append(al)
    areas.append(a)
    t+=1

    b = area(bounds())
    bb =bounds()
    bl = lineyness()

    print "%d: %s -> %s = %d"  % (t, str(aa), str(bb), al-bl)


for node in nodes:
    node.advanceTime(-20000)
    node.advanceTime(liney.index(max(liney)))

showme()

print "Max liney = %d, Min area = %d" % (max(liney), min(areas))
print "At indexes %d ,   %d. " % (liney.index(max(liney)), areas.index(min(areas)))
print "Done drawing."
