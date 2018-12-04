#!/usr/bin/python

inputfile='./inputs/day1a.txt'

frequency = 0

with open(inputfile) as data:
    for line in data.readlines():
        frequency += int(line)

print "Frequency: %d." % frequency
