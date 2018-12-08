#!/usr/bin/python

import string
import re
parsere = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

class Step(object):
    def __init__(self, step, dependencies):
        self.step = step
        self.dependencies = list(dependencies)
    def addDep(self, dep):
        self.dependencies.append(dep)
        self.dependencies = sorted(self.dependencies, reverse=True)

        
    def __repr__(self):
        return "<%s: %s>" % (self.step, str(self.dependencies))


first = None
steps = dict()
with open("inputs/day7-example.txt") as input:
    for line in input.readlines():
        line = line.rstrip()
        (a,b) = parsere.match(line).groups()
        if a in steps:
            steps[a].addDep(b)
            print "Adding dep: %s -> %s." % (a,b)
            print steps[a]
        else:
            steps[a] = Step(a, b)
        if not first:
            first = steps[a]  # Mark the starting step.

for c in string.ascii_uppercase:
    if c not in steps:
        print "%s is undefined." % c
        steps[c] = None
        
def evaluate(step):
    progress = list()
    stack = [step]
    while stack:
        current = stack.pop()
        if current is None: # the last step? Probably, because it is
                            # never claimed as the predecessor.
            continue

        # Avoid duplicates in the stack.
        if not progress or progress[-1] != current.step:
            progress.append(current.step)
        
        stack += [steps[s] for s in current.dependencies]
        stack = sorted(stack)
        #print "Current: %s" % str(current)
        print "Stack: %s" % str(stack)


    return "".join(progress) + steps[progress[-1]].dependencies[0]

progress = list()
print "Steps loaded:"
for step in steps:
    if steps[step]:
        print steps[step]
print evaluate(first)
correct = "CABDFE"
print evaluate(first) == correct
