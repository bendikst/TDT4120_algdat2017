#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(A, B, p, q, r):
    n1 = q - p
    n2 = r - q + 1

    # for i in range(n1):
    #     L[i] = A[p + i - 1]
    # for j in range(n2):
    #     R[i] = A[q + j]
    L = A[p:q]
    R = A[q:r+1]
    #L[n1] = (float('inf'), 'q')
    #R[n2] = (float('inf'), 'q')
    i = 0
    j = 0
    print(L)
    print(R)
    for k in range(0, max(len(L),len(R))):
        if i < n1 and j < n2 and L[i][0] <= R[j][0]:
            #B.append(L[i][0])
            B += L[i][0][1]
            i += 1
        else:
            #B.append(R[j][0])
            B += R[j][0][1]
            j += 1
    print(B)


def merge_sort(decks, result, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(decks, result, p, q)
        merge_sort(decks, result, q + 1, r)
        result = merge(decks, result, p, q, r)
    return result


def merge_to_string(cards):
    result = ''
    for card in cards:
        result += card[1]
    return result


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    result = ''
    result = merge_sort(decks, result, 0, len(decks)-1)
    print(result)


if __name__ == "__main__":
    main()
