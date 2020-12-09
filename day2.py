#!/usr/bin/env python3

inputs = [line.rstrip().split(": ") for line in open("inputs/day2.txt").readlines()]
a_valid = 0
b_valid = 0
for i in inputs:
    (r, c) = i[0].split(' ')
    r = r.split('-')
    i[0] = [int(r[0]), int(r[1]), c]
    cnt = i[1].count(i[0][2])
    if cnt >= i[0][0] and cnt <= i[0][1]:
        a_valid+=1
    if i[1][i[0][0]-1] != i[1][i[0][1]-1] and (i[1][i[0][0]-1] == c or i[1][i[0][1]-1] == c):
        b_valid+=1

print(f"{a_valid} valid (a) passwords.")
print(f"{b_valid} valid (b) passwords.")
