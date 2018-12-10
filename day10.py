#!/usr/bin/python
# Requires wx, I just used `brew install wxpython`.

import re
parsere = re.compile("position=<(.*), (.*)> velocity=<(.*), +(.*)>")

from pprint import pprint

import time

class Node(object):
    def __init__(self, x, y, velx, vely):
        self.x = int(x)
        self.y = int(y)

        self.velx = int(velx)
        self.vely = int(vely)

    def __repr__(self):
        return "<(%d+%d,%d+%d)>" % (
            self.x, self.velx,
            self.y, self.vely)

    def advanceTime(self, t=1):
        self.x += t * self.velx
        self.y += t * self.vely


nodes = list()

with open("inputs/day10-example.txt") as input:
    for line in input.readlines():
        (x, y, velx, vely) = parsere.match(line.rstrip()).groups()
        nodes.append(Node(x,y,velx,vely))


def bounds(nodes=nodes):
    a = sorted(nodes)
    return (a[0].x, a[0].y), (a[-1].x, a[-1].y)


pprint(nodes)

print bounds()

import wx

class Cartesian(wx.Frame):
    def __init__(self, parent=None, id=-1, title=""):
        wx.Frame.__init__(self, parent, id, title, size=(1200, 1200))

        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(event.GetEventObject())
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, width=3))
        #dc.DrawLine(50, 0, 50, 50)
        #dc.DrawLine(0, 50, 50, 50)
        t = 0
        while t < 150:

            t+=1
            for node in nodes:
                dc.SetPen(wx.Pen(wx.WHITE, width=3))
                dc.DrawPoint((node.x+600),(node.y+600))

                node.advanceTime(5)

                dc.SetPen(wx.Pen(wx.BLACK, width=3))
                dc.DrawPoint((node.x+600),(node.y+600))

            #time.sleep(2)
            print "Drawing..."
        print "Done drawing."

app = wx.App(False)
frame = Cartesian()
frame.Show()
app.MainLoop()
