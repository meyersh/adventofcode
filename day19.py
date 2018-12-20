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

def doOp(op, IP, A,B,C, registers=[0,0,0,0,0,0], verbose=False):
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

opcodere = re.compile('(\w+) (\d+) (\d+) (\d+)')
ipre = re.compile('#ip (\d+)')

blanks = 0
ops = list()

for opcode in opcodes:
    if doOp(opcode, 0, 2, 1, 2, [3,2,1,1]) == [3,2,2,1]:
        print('  testing: %s' % opcode)


nums_solved = False
registers = [1,0,0,0,0,0]
ip = 0
ipr = 0 # the register that the ip is bound to.
program = list()
with open("inputs/day19.txt") as input:
    for line in input.readlines():
        line = line.rstrip()

        if ipre.match(line):
            ipr = int(ipre.match(line).groups()[0])
            continue

        if opcodere.match(line):
            (op, a, b, c) = opcodere.match(line).groups()
            a = int(a)
            b = int(b)
            c = int(c)

            program.append((op,a,b,c))


print("Beginning execution.")
print("Program:")
pprint(program)
print("IPR=%d" % ipr)
print("Running...")
while True:

    try:
        (op, a, b, c) = program[ip]
    except IndexError:
        print("PROGRAM HALT!")
        print("IP=%d." % ip)
        break
        
    registers[ipr] = ip    
    registers_after = doOp(op,ip, a,b,c, registers)
    
    print("ip=%04d %s %4s %3d %3d %3d %25s" %
          (ip, str(registers), op, a, b, c,
           str(registers_after)))

    ip = registers_after[ipr]
    registers = registers_after

    ip += 1

print("Registers now: %s" % str(registers))
