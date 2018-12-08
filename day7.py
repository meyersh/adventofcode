#!/usr/bin/python
#
from pprint import pprint
import string
import re

stepre = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

steps = dict()
ases = set()
bses = set()
with open("inputs/day7.txt") as input:
    for line in input.readlines():

        (a,b) = stepre.match(line).groups()

        ases.add(a)
        bses.add(b)

        if b not in steps:
            steps[b] = [a]
        else:
            steps[b] = sorted(steps[b] + [a], reverse=True)


def first():
    d = ases - bses
    try:
        assert len(d) == 1
    except:
        print "Set: %s" % str(d)
    return sorted(list(d))[0]


def evaluate(steps = steps, f = first()):
    ready = sorted([f], reverse=True)
    completed = set([f])
    progress = []
    current = f
    def next():
        nexts = set()
        for (k,v) in steps.items():
            if not v:
                nexts.add(k)
        return sorted(list(nexts))

    def whodependson(c):
        deps = set()
        for (k,v) in steps.items():
            if c in v:
                deps.add(k)
        return sorted(list(deps), reverse=True)

    def markcompleted(c):
        for (k,v) in steps.items():
            if current in v:
                del steps[k][steps[k].index(current)]

    while steps.keys():
        markcompleted(current) # mark it done
        progress.append(current)


        pprint(steps)

        ready += whodependson(current)
        try:
            current = next()[0]
        except:
            pass

        del steps[current]

    progress.append(current)

    return "".join(progress)

correct = "CABDFE"
print "Adding first to steps..."
for s in sorted(list(ases-bses))[1:]:
    steps[s] = []
print "Steps:"
pprint(steps)
print "First available: %s" % first()

print "Evaluating..."
r = evaluate(steps)
print r
print r==correct
