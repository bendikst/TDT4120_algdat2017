from sys import stdin
from itertools import repeat


def mergesort(a):
    n = len(a)
    if n <= 1:
        return a[0]
    else:
        return merge(mergesort(a[:n//2]), mergesort(a[n//2:]))



def merge(l1, l2):
    combined = []
    i, j = 0, 0
    len1, len2 = len(l1), len(l2)
    while i < len1 and j < len2:
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[j])
            j += 1
    combined.extend(l1[i:])
    combined.extend(l2[j:])
    return combined



def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(''.join(char for num, char in mergesort(decks)))


if __name__ == "__main__":
    main()
