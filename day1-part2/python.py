#!/usr/bin/env python3
import sys
import re
from string import digits

words = ('one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine')


def rev_str(line: str) -> str:
    return ''.join(reversed(line))


words_rev = tuple(rev_str(w) for w in words)


def replace_word(match: re.Match[str]) -> str:
    word = match.group(0)
    if len(word) == 1:
        return word
    return str(words.index(word) + 1)


def replace_word_rev(word: re.Match[str]) -> str:
    return str(words_rev.index(word.group(0)) + 1)


rex = re.compile('|'.join(words) + '|' + '|'.join(digits))
rex_rev = re.compile('|'.join(words_rev))

result = 0
for line1 in sys.stdin:
    line = rex.sub(replace_word, line1, 1)
    line = rev_str(rex_rev.sub(replace_word_rev, rev_str(line), 1))
    line = ''.join(c for c in line if c.isdigit())
    result += int(line[0] + line[-1])
print(result)
