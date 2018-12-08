#!/usr/bin/python

from pprint import pprint

def readnode(n, siblings):
    if siblings == 0:
        return None

    nodes = list()
    while siblings:

        meta = list()
        
        nchildren = n.pop(0)
        nmeta = n.pop(0)
        children = readnode(n, nchildren)
        for i in xrange(0, nmeta):
            meta.append(n.pop(0))

        nodes.append({'nchildren': nchildren,
                      'nmeta': nmeta,
                      'children':children,
                      'meta':meta})

        print "Read values: %s" % str(meta)
        siblings -= 1

    return nodes

def readnodes(n):
    n = map(int, n)
    return readnode(n, 1)


#nodes = readnodes("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split())
with open("inputs/day8.txt") as inputs:
    nodes = readnodes(inputs.readline().rstrip().split())


def s(nodes):
    vals = list()
    for node in nodes:
        try:
            print "processing node with meta = %s" % str(node['meta'])
        except:
            print "EXEPTION??"
            
        if node['nchildren'] == 0:
            print "no kinder."
            vals.append(sum(node['meta']))

        else:
            for meta in node['meta']:
                print "processing meta #%d" % meta
                print node['children'][0]
                if  meta-1 < len( node['children']):
                    vals.append(s([node['children'][meta-1]]))
                else:
                    #vals.append(0)
                    continue
                    

    return vals
                

#pprint(nodes)
print "Processing sums..."
total = s(nodes)

# flatten the total. I CANNOT BELIEVE THIS WORKED TOTAL HACK ALERT.
total = sum(map(int,str(total).replace('[', '').replace(']', '').replace(',', '').split()))
            
print "Total = %d " % total
