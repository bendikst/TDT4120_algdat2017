#!/usr/bin/python3

from sys import stdin


def mergesort(A):
    n = len(A)
    if n <= 1:
        return A
    else:
        return merge(mergesort(A[:n//2]), mergesort(A[n//2:]))


def merge(l1, l2):
    combined = []
    i, j, len1, len2 = 0, 0, len(l1), len(l2)
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

    sorted_list = mergesort(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
