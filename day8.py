#!/usr/bin/python
"""
A header, which is always exactly two numbers:
The quantity of child nodes.
The quantity of metadata entries.
Zero or more child nodes (as specified in the header).
One or more metadata entries (as specified in the header).
"""

def readnodesa(n):
    if not n:
        return 0
    
    n = map(int, n)
    print n
    nchildren = n[0]
    nmeta = n[1]
    meta = n[-nmeta:]
    print "Meta: %s" % str(meta)
    remaining = n[2:-nmeta]
    children = 0
    
    if nchildren:
        children = readnodes(remaining)
        
        
    return sum(meta) + children
        
def readnodes(n):
    n = map(int, n)
    n.reverse() # make it a stack so pop() works.

    # Reading nchildren FSM
    rc = True
    children = list()

    # Reading nmeta FSM
    rm = False
    nmeta = list()

    # Reading a meta value FSM
    rv = False
    metavalu = list()
    
    while n:
        #print n
        if rc:
            rc = False
            rm = True
            children.append(n.pop())
            print "Reading a node header: %d children."  % children[-1]


        if rm:
            rm = False
            nmeta.append(n.pop())

            # Are we reading children next or meta values ? 
            if children and children[-1]:
                rc = True
            else:
                rv = True

            print "  --- Reading metadata count: %d" % nmeta[-1]
                            

        if rv:
            reading = nmeta.pop() # How many meta?
            while reading:
                metavalu.append(n.pop())
                reading -= 1

                print "  --- Reading values ", metavalu[-1]

            # We've just read a node. Are we reading nmeta values or
            # headers next?
            if children[-1] == 0:
                print "   No more children: ", children
                children.pop()

            if children:
                children[-1] -= 1                

            if children and children[-1]: # Reading more children

                rv = False
                rc = True
                print "   %d More children to read." % children[-1], children

            else:
                rv = True
                rc = False

                


    print "Done:"
    print "CHILDREN:", children
    print "nmeta:   ", nmeta
    return sum(metavalu)

    
        

print "ACTUAL:"
with open("inputs/day8.txt") as inputs:
    for line in inputs.readlines():
        n = line.rstrip().split()
        print readnodes(n)

#print "EXAMPLE:"
#print readnodes("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split())
