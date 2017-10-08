#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1:
        L = decks.pop(0)
        R = decks.pop(0)
        temp = []
        while L and R:
            if L[0] < R[0]:
                temp.append(L.pop(0))
            else:
                temp.append(R.pop(0))
        temp.extend(L)
        temp.extend(R)
        decks.append(temp)
    letters = [letter for (num, letter) in decks[0]]
    return ''.join(letters)



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
