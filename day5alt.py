#!/usr/bin/python

import re
import string

def checky(a,b):
    if a==b:
        return False
    if a.lower() == b.lower():
        return True
    return False

def reactpolymer(data, verbose=True):
    data = list(data) # Better.
    i = 1
    while i < len(data):
        if checky(data[i-1], data[i]):
            checking = True # Still finding things to delete.
            del data[i]
            del data[i-1]
            i -= 1
            continue
        i += 1
        
    return "".join(data)

def reactpolymer1(data, verbose=True):
    checking = True
    if verbose: print len(data)
    while checking:
        if verbose: print "Iterationing...%d" % len(data)
        checking = False
        deleted = 0
        subtractions=list()
        for i in xrange(0,len(data)-1):

            if checky(data[i], data[i+1]):
                if verbose: print "Removing %s%s." % (data[i],data[i+1])
                data = data[0:i] + data[i+2:]
                checking = True
                deleted += 2

            if i >= len(data)-deleted:
                checking = True
                break
    return data

pairs = list()
for c in string.ascii_lowercase:
    # a, b, c...
    p = [c, c.upper()]
    q = p[::-1]
    pairs.append( "%s|%s" % ("".join(p), "".join(q)) )
    
majorre = re.compile("|".join(pairs))

def reactpolymer2(data, verbose=False):
    reduction = len(data) + 1
    while len(data) < reduction:
        reduction = len(data)
        data = majorre.sub('', data)

    return data


with open("inputs/day5.txt") as inputs:
    data = inputs.readlines()
    data = data[0].rstrip()

    # PART 1
    reacted = reactpolymer(data)
    print "Done... %d units remain." % len(reacted)

    # PART 2
    lowest_reaction = len(data)
    lowest_letter   = None
    for c in string.ascii_lowercase:
        data_redacted = data.replace(c, '').replace(c.upper(), '')
        reaction = reactpolymer(data_redacted, False)
        print "%s...%d" % (c, len(reaction))
        if len(reaction) < lowest_reaction:
            lowest_letter = c
            lowest_reaction = len(reaction)

    print "Lowest reaction length=%d (compound '%s')" % (
        lowest_reaction, lowest_letter)
