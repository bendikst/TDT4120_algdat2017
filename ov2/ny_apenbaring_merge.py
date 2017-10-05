#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    if len(decks) <= 1:
        return ''
    else:
        mid = len(decks)//2
        l = decks[:mid]
        r = decks[mid:]
        result = '' ##

        merge(l)
        merge(r)

        i, j, = 0, 0
        len_l = len(l[0])
        len_r = len(r[0])
        while i < len_l and j < len_r:
            if l[0][i][0] < r[0][j][0]:
                result += l[0][i][1]
                i += 1
            else:
                result += r[0][j][1]
                j += 1

        while i < len_l:
            result += l[0][i][1]
            i += 1

        while j < len_r:
            result += r[0][j][1]
            j += 1
        return result


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(decks)
    print(merge(decks))


if __name__ == "__main__":
    main()
