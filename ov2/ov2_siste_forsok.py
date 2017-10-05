#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        merge(left)
        merge(right)

        i, j, k = 0, 0, 0
        len_l = len(left)
        len_r = len(right)

        while i < len_l and j < len_r:
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len_l:
            A[k] = left[i]
            i += 1
            k += 1

        while j < len_r:
            A[k] = right[j]
            j += 1
            k += 1

def to_str(A):
    result = ''
    for card in A:
        result += card[1]
    return result


def main():
    # Read input.
    # decks = []
    cards = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        cards.extend(deck)
    # Merge the decks and print result.
    merge(cards)
    print(to_str(cards))


if __name__ == "__main__":
    main()
