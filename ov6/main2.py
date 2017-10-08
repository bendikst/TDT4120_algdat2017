#!/usr/bin/python3

from sys import stdin

def max_value(notes, paper_width, paper_height, r):
    size = (paper_width, paper_height) if paper_width < paper_height else (paper_height, paper_width)

    if size in r:
        return r[size]

    q = notes[size] if size in notes else 0

    for x in range(1, paper_width):
        q = max(q, max_value(notes, x, paper_height, r) + max_value(notes, paper_width-x, paper_height, r))

    for y in range(1, paper_height):
        q = max(q, max_value(notes, paper_width, y, r) + max_value(notes, paper_width, paper_height-y, r))

    r[size] = q
    return q

def main():
    notes = {}
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        #value = int(dim_value[1])
        bill = (width, height) if width < height else (height, width)

        if bill in notes:
            notes[bill] = max(int(dim_value[1]), notes[bill])
        else:
            notes[bill] = int(dim_value[1])

    r = {}
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(notes, paper_width, paper_height, r)))


if __name__ == "__main__":
    main()
