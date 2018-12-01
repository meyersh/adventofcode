#!/usr/bin/python

inputfile='./inputs/day1a.txt'

iterations = 0
frequency = 0
seen = set()
duplicate_frequency = "none"

with open(inputfile) as data:
    frequencies = [int(x.rstrip()) for x in data.readlines()]

while duplicate_frequency == "none":
    iterations += 1
    print "%d time through." % iterations
    for change in frequencies:
        frequency += change
        if frequency not in seen:
            seen.add(frequency)
        else:
            print "Duplicate frequency: %d" % frequency
            duplicate_frequency = frequency
            break

print "Frequency: %d." % frequency
