#!/usr/bin/python

with open("inputs/day2.txt") as inputs:
    data = [x.rstrip() for x in inputs.readlines()]

def dubstrips(s):
    occurrences = dict()
    pairs = trips = 0
    
    for c in s:
        if c not in occurrences:
            occurrences[c] = 1
        else:
            occurrences[c] += 1

    for k in occurrences:
        if occurrences[k] == 2:
            pairs = 1
        if occurrences[k] == 3:
            trips = 1

    return (pairs,trips)
    
pairs = 0
trips = 0
    
for d in data:
    two,three = dubstrips(d)
    pairs += two
    trips += three

print "pairs: %d trips: %d total: %d" % (
    pairs, trips, pairs * trips)

