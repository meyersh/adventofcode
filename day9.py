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
    value   = 1 # next marble's number (in the "bank")
    marbles = deque([0]) # that first marble in there.
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
