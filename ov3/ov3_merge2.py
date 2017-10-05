#!/usr/bin/python3

from sys import stdin
from random import randint


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)
    return A


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i+1

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def binary_search(A, value):
    l, r = 0, len(A)-1
    while l <= r:
        m = (l + r) // 2
        if value == A[m]:
            break
        elif value < A[m]:
            r = m - 1
        else:
            l = m + 1
    return m


def find(A, lower, upper):
    indeks_lower = binary_search(A, lower)
    indeks_upper = binary_search(A, upper)
    if A[indeks_lower] > lower and indeks_lower != 0:
        indeks_lower -= 1
    if A[indeks_upper] < upper and indeks_upper != len(A) - 1:
        indeks_upper += 1
    return [A[indeks_lower], A[indeks_upper]]

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = randomized_quicksort(input_list, 0, len(input_list)-1)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
