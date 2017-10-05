#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1: #raskere enn len()?
        l = decks.pop(0)
        r = decks.pop(0)
        temp = []
        while r and l:
            if l[0] < r[0]:
                temp.append(l.pop(0))
            else:
                temp.append(r.pop(0))
        temp.extend(l)
        temp.extend(r)
        decks.append(temp)
    result = ''
    for (number, letter) in decks[0]:
        result += letter
    return result

def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
