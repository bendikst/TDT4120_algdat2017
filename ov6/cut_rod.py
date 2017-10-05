#!/usr/bin/python3

from sys import stdin


def memoized_cut_paper(paper_width, paper_height, widths, heights, values, indeks):
    r = [-float('inf')]*indeks
    return mcp_aux(paper_width, paper_height, widths, heights, indeks-1, values, r)


def mcp_aux(paper_width, paper_height, widths, heights, indeks, values, r):
    # print(widths)
    # print(heights)
    # print(values)
    # print(r)
    print(r)
    if r[indeks] >= 0:
        return r[indeks]
    if indeks == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(indeks+1):
            q = max(q, values[i] + mcp_aux(paper_width, paper_height, widths, heights, indeks-1, values, r))

    r[indeks] = q
    return q



def max_value(widths, heights, values, paper_width, paper_height):
    return memoized_cut_paper(paper_width, paper_height, widths, heights, values, len(values))

def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()
