#!/usr/bin/python
import re
parsere = re.compile("(\d+) players; last marble is worth (\d+) points")

from pprint import pprint
from collections import deque

def playthegameDeque(players, lastmarblepoints):
    playerscores = dict()
    for i in xrange(0, players):
        playerscores[i] = 0

    currentplayer = 0 # current player index
    current = 0  # current marble index
    value   = 1 # next marble's number (in the "bank")
    marbles = deque([0]) # that first marble in there.
    turn    = 0 # player n's turn.
    while value <= lastmarblepoints:
        #print marbles
        if value % 23: # NOT divisible by 23... proceed normally.
            marbles.rotate(1)
            marbles.appendleft(value)
            
        else: # Something entirely different happens when its divisible by
              # 23...

            playerscores[currentplayer] += value # keep the value they would have laid.

            marbles.rotate(-7)
            playerscores[currentplayer] += marbles.popleft()
            marbles.rotate(1)


        # At the end of the round, advance some ticks.
        turn += 1
        value += 1
        currentplayer = (currentplayer + 1) % players
            
    return playerscores

def playthegame(players, lastmarblepoints):
    playerscores = dict()
    for i in xrange(0, players):
        playerscores[i] = 0

    currentplayer = 0 # current player index
    current = 0  # current marble index
    value   = 1 # next marble's number (in the "bank")
    marbles = [0] # that first marble in there.
    turn    = 0 # player n's turn.
    while value <= lastmarblepoints:
        #print marbles
        if value % 23: # NOT divisible by 23... proceed normally.
            insertion = (current+2) % len(marbles)
            marbles.insert(insertion, value)
            current = insertion # we just "laid" it.

        else: # Something entirely different happens when its divisible by
              # 23...

            playerscores[currentplayer] += value # keep the value they would have laid.


            # Remove the marble 7 places ccw.
            cw = marbles[(current-6) % len(marbles)] # note the marble value
                                                     # cw of what we're removing.
            playerscores[currentplayer] += marbles[(current-7) % len(marbles)]
            current = (current - 8) % len(marbles)
            del marbles[(current - 7) % len(marbles)]
            current = (current +1) % len(marbles)
            # New current marble, 6 ccw (-1 because our pool shrunk by
            # one.)  Still often off by one (see exception/assertion
            # block below) We correct for this by using the cw
            # "value-of" to find the correct one. EXPENSIVE but it works.


            try:
                assert current == marbles.index(cw)
            except AssertionError:
                print "(%d marbles) Current v cw: %d v %d." % (len(marbles), current, marbles.index(cw))                

            current = marbles.index(cw)



        # At the end of the round, advance some ticks.
        turn += 1
        value += 1
        currentplayer = (currentplayer + 1) % players
            
    return playerscores

with open("inputs/day9.txt") as input:
    for line in input.readlines():
        try:
            (players, lastmarblepoints) = parsere.match(line.rstrip()).groups()
        except AttributeError:
            continue
            
        players = int(players)
        lastmarblepoints = int(lastmarblepoints)
        print "%d players , last marble worth %d points: high score %d" % (
            players,
            lastmarblepoints,
            max(playthegameDeque(players,lastmarblepoints).values()))
        



# part b... what would it be if it were 100 times higher?
print "%d players , last marble worth %d points: high score %d" % (
    players,
    lastmarblepoints,
    max(playthegameDeque(players,lastmarblepoints*100).values()))
