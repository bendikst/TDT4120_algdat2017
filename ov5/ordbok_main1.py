#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

#TESTFUNKSJON!!
'''
def print_tree(tree):
    for i in range (3):
        if tree.barn != None:
            print(tree.barn.items())
'''

def bygg(ordliste):
    head = Node()
    for word, pos in ordliste:
        head.barn[word[0]] = recursive_tree_build(head, word, 0, pos)
    return head


def recursive_tree_build(tree, word, depth, pos):
    if depth >= len(word):
        tree.posi.append(pos)
        return tree
    else:
        tree.barn[word[depth]] = Node()
        return recursive_tree_build(tree.barn[word[depth]], word, depth + 1, pos)


def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER
    pass

def main():
    try:
        word = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in word:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        print(toppnode.barn['e'].barn.keys())
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
