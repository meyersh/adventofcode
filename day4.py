#!/usr/bin/python

import re
shiftbeginre = re.compile(r"\[(.*)\] Guard #([0-9]+) begins shift")
sleepbeginre = re.compile(r"\[(.*)\] falls asleep")
wakeupre     = re.compile(r"\[(.*)\] wakes up")

from datetime import datetime, timedelta
from pprint import pprint

def timestamp(ts):
    # Decode yyyy-mm-dd hh:mm as necessary.
    #fmt = "%Y-%m-%d %H:%M"
    fmt = "%H:%M"
    ts = ts.split(" ")[1] # only consider the time.
    return datetime.strptime(ts, fmt)

guards = dict()

with open("inputs/day4.txt-sorted") as inputs:
    awake = 1
    guardid = None
    for line in inputs.readlines():
        line = line.rstrip()
        if shiftbeginre.match(line):
            awake = 1
            guardid = shiftbeginre.match(line).groups()[1]
        if sleepbeginre.match(line):
            awake = 0
            startsleeping = timestamp(sleepbeginre.match(line).groups()[0])
            
        if wakeupre.match(line):
            awake = 1
            endsleeping = timestamp(wakeupre.match(line).groups()[0])
            # print guardid, startsleeping, endsleeping
            if guardid not in guards:
                guards[guardid] = []
            guards[guardid].append((startsleeping, endsleeping - startsleeping))

# pprint(guards)

def sumtime(times):
    sum = 0
    for (start,delta) in times:
        sum += delta.seconds / 60
    return sum

mostsleepy = None
mostminutes = 0
for guard in guards:
    if sumtime(guards[guard]) > mostminutes:
        mostsleepy = guard
        mostminutes = sumtime(guards[guard])

def heatmapper(guard=mostsleepy, show=False):
    heatmap = dict()
    for minute in xrange(0,59):
        heatmap[minute] = 0
    for (time,delta) in guards[guard]:
        if show: print "%d to %d." % (time.minute, time.minute+(delta.total_seconds()/60))
        for minute in xrange(time.minute, time.minute+(delta.seconds/60)): #-1 ?
            heatmap[minute] += 1

    maxminute = 0
    occurrences = 0
    for minute in heatmap:
        if show: print "%2d: " % minute,
        if heatmap[minute] > occurrences:
            maxminute = minute
            occurrences = heatmap[minute]
        for x in xrange(heatmap[minute]):
            if show: print "x",
        if show: print ""

    return (heatmap, maxminute)

(heatmap, maxminute) = heatmapper(guard=mostsleepy)
print "(PART 1)"
print "Most sleepy = %d (minutes), Guard = #%s" % (mostminutes, mostsleepy)
print "Most popular minute = %d" % maxminute
print "%s * %d = %d" % (mostsleepy, maxminute, int(mostsleepy)*maxminute)

mostpopminute = None
mostoccurrences = 0
popsleeper = None
for guard in guards:
    (heatmap,maxminute) = heatmapper(guard)
    if heatmap[maxminute] > mostoccurrences:
        mostpopminute = maxminute
        popsleeper = guard
        mostoccurrences = heatmap[maxminute]

print "(PART 2)"
print "Most popular sleeping minute is :%d by guard #%s with %d naps." % (
    mostpopminute, popsleeper, mostoccurrences)
print "%s * %d = %d" % (
    popsleeper,
    mostpopminute,
    int(popsleeper)*mostpopminute)

# pprint(heatmapper("99"))
