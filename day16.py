#!/usr/bin/env python3

# Opcode party time.

opcodes = ('addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr',
           'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri',
           'eqrr')

opcode_base = {
    'add': lambda a,b: a+b,
    'mul': lambda a,b: a*b,
    'ban': lambda a,b:a&b,
    'bor': lambda a,b:a|b,
    'set': lambda a,b:a,
    'gti': lambda a,b:1 if a>b else 0,
    'gtr': lambda a,b:1 if a>b else 0,
    'eqi': lambda a,b:1 if a==b else 0,
    'eqr': lambda a,b:1 if a==b else 0,
    }

def doOp(op, A,B,C, registers=[0,0,0,0], verbose=False):
    myregisters = registers.copy()
    # Doing a register instruction or immediate?
    if  op not in ('seti', 'gtir', 'eqir'):
        a = myregisters[A]
    else:
        a = A
    
    if op[-1] == 'r':
        b = myregisters[B]
    else:
        b = B #  "value' b.

    myregisters[C] = opcode_base[op[:-1]](a,b)

    if verbose:
        print("%s A:%d B:%d C:%d -> %s" % (op, A, B, C, str(registers)))
    
    return myregisters

blanks = 0

import re
from pprint import pprint

beforere = re.compile('Before: (.*)')
afterre = re.compile('After:  (.*)')
opcodere = re.compile('(\d+) (\d+) (\d+) (\d+)')

blanks = 0
ops = list()

for opcode in opcodes:
    if doOp(opcode, 2, 1, 2, [3,2,1,1]) == [3,2,2,1]:
        print('  testing: %s' % opcode)


# part two processing...
def solveOpNums(opcode_nums):
    while sum([len(x) for x in opcode_nums.values()]) != len(opcode_nums.keys()):
        for op in opcode_nums.keys():
            if len(opcode_nums[op]) > 1: continue
            identified_op = opcode_nums[op].pop()
            print("Identified %s"%identified_op)
            opcode_nums[op].add(identified_op)

            # Remove this op from all other possibilities.
            for op2 in opcode_nums.keys():
                if op2 == op: continue

                opcode_nums[op2].discard(identified_op)

    for op in opcode_nums:
        opcode_nums[op] = opcode_nums[op].pop()

    return opcode_nums

nums_solved = False
samples = 0
opcode_nums = dict()
registers = [0,0,0,0]

with open("inputs/day16.txt") as input:
    for line in input.readlines():
        line = line.rstrip()
        #print(line)
        

        if beforere.match(line):
            blanks = 0
            before = [x for x in map(int, eval(beforere.match(line).groups()[0]))]

        elif afterre.match(line):
            after = [x for x in map(int,eval(afterre.match(line).groups()[0]))]
            acts_like = list()
            
            for opcode in opcodes:
                if opcode in opcode_nums.values():
                    continue
                if doOp(opcode, a,b,c, before) == after:
                    #print('%s matches! %s -> %s' % (opcode, str(before), str(after)))
                    acts_like.append(opcode)
            if len(acts_like) >= 3:
                samples += 1

            if op not in opcode_nums:
                opcode_nums[op] = set()
            [opcode_nums[op].add(x) for x in acts_like]
            #print(acts_like)

                
        elif opcodere.match(line):
            if blanks > 2:
                (op, a, b, c)  = map(int, opcodere.match(line).groups())
                if not nums_solved:
                    opcode_nums = solveOpNums(opcode_nums)
                    nums_solved = True
                    
                #print("Processing %s." % line)
                registers = doOp(opcode_nums[op], a,b,c,
                                 registers=registers, verbose=False)
            else:
                (op, a, b, c)  = map(int, opcodere.match(line).groups())

        elif not line:
            blanks += 1
            #print()

        else:
            print('Line: "%s"' %line)

print("%d samples act like 3 or more opcodes." % samples)
    
pprint(opcode_nums)
print("Registers now: %s" % str(registers))
