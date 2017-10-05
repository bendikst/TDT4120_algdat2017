#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    head = Node()
    for word, pos in ordliste:
        node = head
        for letter in word:
            if letter not in node.barn:
                node.barn[letter] = Node()
            node = node.barn[letter]
        node.posi.append(pos)
    return head


def posisjoner(ord, indeks, node):
    if indeks >= len(ord):
        return node.posi
    elif ord[indeks] == '?':
        test = []
        #test.extend((posisjoner(ord, indeks+1, child) for child in node.barn.values()))
        #return [pos for pos in posisjoner(ord, indeks+1, barn) for barn in node.barn.values()]
        for child in node.barn.values():
            test += posisjoner(ord, indeks+1, child)
        return test
    elif ord[indeks] in node.barn:
        return posisjoner(ord, indeks+1, node.barn[ord[indeks]])
    else:
        return []


def main():
    try:
        word = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in word:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()
