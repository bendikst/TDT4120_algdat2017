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


def find(A, lower, upper):
    if A[0] > lower:
        a_lower = A[0]
    else:
        L, R = 0, len(A)-1
        while R > L:
            mid =  (L+R) // 2
            if A[mid] < lower:
                L = mid + 1
            elif A[mid] > lower:
                R = mid - 1
            else:
                break
        if A[mid] > lower and mid !=0:
            mid -= 1
    a_lower = A[mid]


    if A[-1] < upper:
        return [a_lower, A[-1]]

    L, R = 0, len(A)-1
    while L <= R:
        mid = (L+R) // 2
        if A[mid] == upper:
            break
        elif upper < A[mid]:
            R = mid - 1
        else:
            L = mid + 1

    if A[mid] < upper and mid != len(A) - 1:
        mid += 1

    return [a_lower, A[mid]]



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
