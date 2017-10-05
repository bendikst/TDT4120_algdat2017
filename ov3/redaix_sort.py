#!/usr/bin/python3

from sys import stdin
#from collections import defaultdict


def counting_sort(A, exp1):
    n = len(A)
    B, C = [0] * n, [0] * 10
    for i in range(n):
        C[(A[i]//(10**exp1)) % 10] += 1
    for j in range(1, 10):
        C[j] += C[j - 1]

    for k in range(n - 1, -1, -1):
        B[C[(A[k]//(10**exp1))%10]-1] = A[k]
        C[(A[k]//(10**exp1))%10] -= 1

    return B



def radix_sort(A, d):
    for i in range(d):
        A = counting_sort(A, i)
    return A


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

    sorted_list = radix_sort(input_list, 6)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
