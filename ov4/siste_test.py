#!/usr/bin/python3

from sys import stdin
from collections import defaultdict
from operator import itemgetter


def flexradix(A, d):
    if len(A) <= 1:
        return A

    letter_buckets = defaultdict(list)

    for string in A:
        if d >= len(string):
            pass
    else:
        letter_buckets[string[d]].append(string)
        print(letter_buckets)

    letter_buckets = [flexradix(bucket, d + 1) for key, bucket in letter_buckets.items()]
    print(letter_buckets)
    return [string in letter_buckets]



def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, 0)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
