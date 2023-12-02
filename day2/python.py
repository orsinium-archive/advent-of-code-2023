#!/usr/bin/env python3
import sys


LIMITS = dict(red=12, green=13, blue=14)


def round_possible(line: str) -> bool:
    for part in line.split(','):
        count, color = part.split()
        if int(count) > LIMITS[color]:
            return False
    return True


possible_sum = 0
for line in sys.stdin:
    game_name, line = line.split(':')
    rounds = line.split(';')
    if all(round_possible(r) for r in rounds):
        game_id = int(game_name.split()[-1])
        possible_sum += game_id
print(possible_sum)
