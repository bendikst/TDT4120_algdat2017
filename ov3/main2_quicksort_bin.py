#!/usr/bin/python3

from sys import stdin


def sort_list(A): #quicksort
    if A == []:
        return []
    else:
        pivot = A[0]
        less = sort_list([x for x in A[1:] if x < pivot])
        more = sort_list([x for x in A[1:] if x >= pivot])
        return less + [pivot] + more


def find(A, nedre, ovre):
    indeks_nedre = binary_s(A, nedre)
    indeks_ovre = binary_s(A, ovre)
    if A[indeks_nedre] > nedre and indeks_nedre != 0:
        indeks_nedre -= 1
    if A[indeks_ovre] < ovre and indeks_ovre != len(A) - 1:
        indeks_ovre += 1
    return [A[indeks_nedre], A[indeks_ovre]]


def binary_s(A, value):
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


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
