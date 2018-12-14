#!/usr/bin/env python3

pots = 0
rules = dict()

with open("inputs/day12.txt") as input:
    initial_state = input.readline().rstrip().split(':')[1].lstrip()
    print("Initial State:\n  '%s' @ %d chars." % (initial_state, len(initial_state)))
    # Read in the pots
    for c in initial_state:
        if c == ' ': continue
        pots = pots << 1
        if c == '#':
            pots += 1

    # Read in the conditions.
    for line in input.readlines():
        line = line.rstrip()
        if not line:
            continue

        (pattern, result) = line.split(" => ")
        pattern = pattern.replace('#', '1').replace('.', '0')
        p = 0
        for c in pattern:
            p = p << 1

            if int(c):
                p += 1

        rules[p] = True if result == '#' else False
        #print( bin(p))


p = pots
n = 0
ones = 1
while p:
    p = p >> 1
    n += 1
    ones += 1

print("%d places in the pots array." % n)
def comparer2(pots, rule, effect, verbose=False):
    t = pots # temp
    n = 0
    while t:
        t = t >> 1
        n += 1
    
    for i in range(0,n):
        local = (pots & (31 << i))
        localrule = rule << i
        if verbose:
            print("Trying: %s" % str(bin(local)))
            print("      : %s"% str(bin(localrule)))
        if local & localrule == local | localrule:
            if verbose:
                print("Match!: %s" % str(bin(local)))
                print("      : %s"% str(bin(localrule)))

            return (effect << i)

    return 0 # Nothing to do.

def comparer(pots, rule, verbose=False):
    global n
    matches = 0 # return value. Ones for every position matched.
    location = 1<<3 # Priming initial position.
    t = pots << 3 # clear the rhs for our initial comparison.
    mask = 0b11111
    while t:
        if (t&mask) == rule:
            matches = matches|location
            if verbose:
                print("t:    {:b}".format(t))
                print("match: ({:05b})".format(t&mask))
        t = t >> 1
        location = location << 1

    return matches >> 3 # we were offset, remember?
        
    
#print(bin(comparer(pots,0b01000, 1)))
#print(bin(pots))

def prettyprint(pots=pots, n=n):
    # we're used to seeing #....## so this'll make things simpler.
    return "{:b}".format(pots).replace("1", "#").replace("0", ".")

def q(n, i):
    """return the bit (True / False) of the i'th bit of n, numbered from
    the right, zero-indexed."""
    if n & (1<<i):
        return True
    return False


def nones(pots=pots):
    t = pots  # temp
    n = 0
    while t:
        if t & 1:
            n +=1
        t = t >> 1
    return n

def countPotNums(pots,n):
    """Our puzzle input starts at n, where n is the number 0th
    pot. Positive numbers to the right and negative numbers to the
    left. We want the sum of the numbers having plants (the ones from our
    binary "pots" value. Whew."""

    i = n-1 # index value. Ugly, I know. (zero indexed, right?)
    t = pots
    total = 0
    while t:
        if t&1:
            total += i
        t = t >> 1 

        i = i - 1

    return total

# Some rules do nothing, so no point checking against them.
# Here we find those rules and remove them from rules[].
noeffect = list()
for rule in rules:

    growing = q(rule, 2)
    if (growing is False and rules[rule] is False) or (growing and rules[rule]):
        state = "No Change."
        noeffect.append(rule)
        continue
    if growing is True and rules[rule] is False:
        state = "Death."
    if growing is False and rules[rule] is True:
        state = "New Growth."

    print('{:5s}: {:#07b} (Growing = {:5s}) -> {:s}'.format(
        str(rules[rule]), rule, str(growing), state))

# Re-consider noops.
#for rule in noeffect:
#    del rules[rule]
    
print("%d rules can have any effect. (%d noops removed.)" % (len(rules), len(noeffect)))
print("Current: %d pots growing." % nones(pots))

print("Pots:")
#print(bin(pots))
for generation in range(1,501):
    n += 1 # the digits keep growing each generation.
    grows = 0
    kills = 0
    for rule in rules:
        p = comparer(pots, rule, verbose=False)
        if p:
            if rules[rule]:
                grows = grows | p
            else: 
                kills = kills | p

    potsa = pots
    #pots = (pots|grows) - kills
    pots = grows

    print("Generation: %05d. Sum = %06d @  %d Grows / %d Kills." % (
        generation, countPotNums(pots,n), nones(grows), nones(kills)))

    #print("Potsa: {:028b}".format(potsa))
    #print("Grows: {:028b}".format(grows))
    #print("Kills: {:028b}".format(kills))
    #print("Potsb: {:028b}".format(pots))
    #print(prettyprint(pots))

print("Finally: %d pots growing." % nones(pots))
print("n=%d should be pot 0." % n)
print("So, our total is: %d." % countPotNums(pots, n))
# 1396 TOO LOW.

print("Begin testing...")
rule = 0b01000
pots = 0b0001000100001000001001001001
print("{:b}".format(comparer(pots,rule, True)))
# 3491+(50000000000-100)*25 = 1,250,000,000,991
# At a certain generation, things have stabilized So...
# stable score = 3491 (at generation 100), and thereafter increasing by
# 25 (on my input) means the total is initial + (50B - generations)*25.
# To detect this, we'll need to check for the generations to stabilize.
