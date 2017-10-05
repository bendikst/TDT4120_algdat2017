#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def build_min_heap(decks):
    for i in range((len(decks)-1)//2, 0, -1):
        card_sink(decks)
    return decks


def card_sink(decks):#ekstra
    i = 0
    while i < len(decks) - 1 and decks[i][0][0] > decks[i + 1][0][0]:
        decks[i], decks[i + 1] = decks[i + 1], decks[i]
        i += 1


def merge(decks):
    result = ''
    while decks:
        result += decks[0][0][1]
        if len(decks[0]) > 1:
            del decks[0][0]
        else:
            del decks[0]
        card_sink(decks)
    return result


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    build_min_heap(decks)#ekstra
    print(merge(decks))


if __name__ == "__main__":
    main()
