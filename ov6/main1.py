#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    result_val = 0
    widths.sort()
    heights.sort()
    values.sort() #Vil dette gå på en smell?
    for i in range(len(values)-1, -1, -1):
        while True:
            if paper_width >= widths[i] and paper_height >= heights[i]:
                result_val += values[i]
                paper_width -= widths[i]
                paper_height -= heights[i]
                print('width')
            elif paper_width >= heights[i] and paper_height >= widths[i]:
                result_val += values[i]
                paper_width -= heights[i]
                paper_height -= widths[i]
                print('height')
            else:
                print('break')
                break
    return result_val


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
