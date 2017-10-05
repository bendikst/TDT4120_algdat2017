#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d):
    bits_per_gruppe = 8
    bits_brukt = 0
    maksverdi = 0



def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        word = line.rstrip()
        strings.append(word)
    A = flexradix(strings, 0)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
