#!/usr/bin/env python3
import sys


total = 0
for line in sys.stdin:
    winning, mine = line.split(':')[1].split('|')
    matches = len(set(winning.split()) & set(mine.split()))
    if matches:
        total += 2 ** (matches - 1)
print(total)
