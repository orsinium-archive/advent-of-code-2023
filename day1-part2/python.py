#!/usr/bin/env python3
import sys
import re


def rev_str(line: str) -> str:
    return ''.join(reversed(line))


def get_replacement_map() -> dict[str, int]:
    words = ('one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine')
    word_map = {w: i for i, w in enumerate(words, start=1)}
    for i in range(1, 10):
        word_map[str(i)] = i
    for i, w in enumerate(words, start=1):
        word_map[rev_str(w)] = i
    return word_map


# The map looks like this:
#   {'one': 1, 'two': 2, ..., '1': 1, '2': 2, ..., 'eno': 1, 'owt': 2, ...}
word_map = get_replacement_map()


def replace_word(match: re.Match[str]) -> str:
    return str(word_map[match.group(0)])


rex = re.compile('|'.join(word_map))

result = 0
for line1 in sys.stdin:
    # replace the first match
    line = rex.sub(replace_word, line1, 1)
    # replace the last match in a reversed string and reverse it back
    line = rev_str(rex.sub(replace_word, rev_str(line), 1))
    # filter out digits only
    line = ''.join(c for c in line if c.isdigit())
    # take the first and the last digit
    result += int(line[0] + line[-1])
print(result)
