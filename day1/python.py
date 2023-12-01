#!/usr/bin/env python3
import sys

result = 0
for line in sys.stdin:
    line = ''.join(c for c in line if c.isdigit())
    result += int(line[0] + line[-1])
print(result)
