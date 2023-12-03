#!/usr/bin/env python3
import re
import sys


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'


def get_good_coords(lines: list[str]) -> set[tuple[int, int]]:
    good_coords = set()
    for lineno, line in enumerate(lines):
        line = line.removesuffix('\n')
        for col, char in enumerate(line):
            if is_symbol(char):
                for y in [lineno - 1, lineno, lineno+1]:
                    for x in [col - 1, col, col+1]:
                        if x >= 0 and y >= 0:
                            good_coords.add((y, x))
    return good_coords


def main() -> int:
    lines = list(sys.stdin)
    good_coords = get_good_coords(lines)

    result = 0
    rex = re.compile(r'[0-9]+')
    for lineno, line in enumerate(lines):
        for match in rex.finditer(line):
            cols = range(match.start(), match.end())
            if any((lineno, col) in good_coords for col in cols):
                number = match.group(0)
                result += int(number)
    return result


print(main())
# 539590
