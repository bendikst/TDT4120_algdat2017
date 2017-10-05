#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def min_heapify(decks, i):
    l = 2*(i)
    r = 2*(i) + 1
    if l < len(decks) and decks[l][0][0] < decks[i][0][0]:
        min = l
    else :
        min = i
    if r < len(decks) and decks[r][0][0] < decks[min][0][0]:
        min = r
    if min != i:
        decks[i], decks[min] = decks[min], decks[i]
        min_heapify(decks, min)
    return decks


def build_min_heap(decks):
    for i in range((len(decks)-1)//2, 0, -1):
        decks = min_heapify(decks, i)
    return decks


def merge(decks):
    result = ''
    while len(decks) > 1:
        result += decks[1][0][1]
        if len(decks[1]) > 1:
            del decks[1][0]
        else:
            del decks[1]
        #decks = min_heapify(decks, 1)
        for i in range((len(decks)-1)//2, 0, -1):
            decks = min_heapify(decks, i)
    return result


def main():
    # Read input.
    decks = [None]
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    decks = build_min_heap(decks)
    print(merge(decks))


if __name__ == "__main__":
    main()
