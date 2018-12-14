#!/usr/bin/env python3

from pprint import pprint
import copy

with open("inputs/day13.txt") as input:
    gridy = [list(line.rstrip()) for line in input.readlines()]
    track = copy.deepcopy(gridy)

# Make the track by removing all carts (assume carts aren't on
# intersections.)
for y in range(0,len(track)):
    for x in range(0,len(track[y])):
        if track[y][x] in "<>":
            track[y][x] = '-'
        if track[y][x] in "v^":
            track[y][x] = '|'
            
class Cart():
    def __init__(self, x, y):
        self.turns = 0
        self.x = x
        self.y = y
        self.active = True

    def __repr__(self):
        return "<Cart: %d turns @ (%d,%d) (Active:%s)>" % (
            self.turns, self.x, self.y, str(self.active))

def prettyprint(grid=gridy):        
    for y in range(0,len(gridy)):
        for x in range(0,len(gridy[y])):
            print(grid[y][x], end="")

        print()

cartshapes = ('^', '>', 'v', '<')

def findcarts(gridy=gridy):
    carts = list()
    for y in range(0,len(gridy)):
        for x in range(0,len(gridy[y])):
            if gridy[y][x] in cartshapes:
                carts.append((x,y))

    return carts

carts = [Cart(cart[0], cart[1]) for cart in findcarts()]

pprint(carts)

def left(c):
    return cartshapes[(cartshapes.index(c) - 1) % 4]

def right(c):
    return cartshapes[(cartshapes.index(c) + 1) % 4]

"""
horizontal piece repairs WHEN:

1: ---
2: \-/
3: +-+
4: \-\
5: /-/
6: /-\

vertical piece repairs when:

|  +  \
|  |  |
|  +  /  ...



"""
def repair(x,y):
    global track
    return track[y][x]


def tick(gridy=gridy, verbose=False, stoponcrash=True):

    for cart in sorted(carts, key=lambda cart: (cart.y, cart.x)):
        if not cart.active:
            continue
        if verbose: print("Moving cart %s." % str((cart.x, cart.y)))
        c = gridy[cart.y][cart.x] # directionish.

        # Get the next coordinate.
        if c == '>':
            nextx = cart.x + 1
            nexty = cart.y
        elif c == '<':
            nextx = cart.x - 1
            nexty = cart.y
        elif c == '^':
            nextx = cart.x
            nexty = cart.y - 1
        elif c == 'v':
            nextx = cart.x
            nexty = cart.y + 1
        else:
            print("Struggling, looking at c '%s' in %s " % (c, cart))

        # Handle intersections
        if gridy[nexty][nextx] == '+':
            # We turn left, straight, right, over and over.
            if cart.turns % 3 == 0:
                c = left(c)
            elif cart.turns % 3 == 1:
                c = c # nothing changes, go straight.
            elif cart.turns % 3 == 2:
                c = right(c)

            cart.turns += 1
            

        # Handle curves
        if gridy[nexty][nextx] == '\\':
            if c in ('>', '<'):
                c = right(c)
            else:
                c= left(c)

        if gridy[nexty][nextx] == '/':
            if c in ('<', '>'):
                c = left(c)
            else:
                c = right(c)


        # Handle straight line bits.
        if gridy[nexty][nextx] in ('-', '|'):
            pass

        if gridy[nexty][nextx] in cartshapes:
            if stoponcrash:
                gridy[nexty][nextx] = "X"
                print("TERRIBLE CRASH: %s" % str((nextx,nexty)))
                return False
            else:
                gridy[nexty][nextx] = repair(nextx, nexty)
                gridy[cart.y][cart.x] = repair(cart.x, cart.y)
                cart.active = False
                cart.x = nextx
                cart.y = nexty
                for othercart in carts:
                    if othercart.x == nextx and othercart.y == nexty:
                        othercart.active = False
                return True
                        

        # Otherwise, move the cart and repair the carts previous
        # location with new track.

        # Omit this to leave streamers...
        gridy[cart.y][cart.x] = repair(cart.x,cart.y)
        assert gridy[cart.y][cart.x] is not None
        
        cart.x = nextx
        cart.y = nexty

        gridy[nexty][nextx] = c

    return True


n=0


###
### PARTY TIME
###

### PART 1

#while tick():
#    n+=1
#    prettyprint()
#    print("tock..%d"%n)
#    print(sorted(carts, key=lambda cart: (cart.y, cart.x)))
#    print("TURNS: %s" % " ".join(["{:04d}".format(cart.turns) for cart in carts]))


# NOT 19,136.
# NOT 93,80...
# NOT 127,117
# NOT 104,30
# NOT 103,30

### PART 2


while len(carts)> 1:
    n+=1
    print("tock..%d"%n)
    print(sorted(carts, key=lambda cart: (cart.y, cart.x)))
    print("TURNS: %s" % " ".join(["{:04d}".format(cart.turns) for cart in carts]))
    carts = [c for c in carts if c.active]
    tick(stoponcrash=False)
# NOT 118,104
# NOT 117,103
# NOT 119,104...
# NOT 53,20
print(carts)
