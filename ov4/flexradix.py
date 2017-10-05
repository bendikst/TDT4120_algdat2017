#!/usr/bin/python3

from sys import stdin


def flexradix(A, d):
    if len(A) <= 1:
        return A

    done_bucket = []
    letter_buckets = [[] for x in range(27)]

    for string in A:
        if d >= len(string):
            done_bucket.append(string)
        else:
            letter_buckets[ord(string[d]) - ord('a')].append(string)

    letter_buckets = [flexradix(bucket, d + 1) for bucket in letter_buckets]
    return done_bucket + [b for blist in letter_buckets for b in blist]


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
