#!/usr/bin/env python3

nums = [int(line.rstrip()) for line in open("inputs/day1a.txt").readlines()]

for i in range(0, len(nums)):
    needle = 2020 - nums[i]
    for j in range(i, len(nums)):
        if nums[j] == needle:
            print(f"{nums[i]} + {nums[j]} = {nums[i] + nums[j]}")
            print(f"{nums[i]} * {nums[j]} = {nums[i] * nums[j]}")
