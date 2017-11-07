from sys import stdin
from heapq import heappush, heappop

Inf = float(1e3000)

def mst(n, nm):
    unchecked = [1]*n
    count, maxi = 1, 0
    heap_road = []
    minimum_road = [Inf]*n
    for i in range(len(nm[0])):
        heappush(heap_road, (nm[0][i], i))
        minimum_road[i] = nm[0][i]
    unchecked[0] = 0
    while count < n:
        m, indeks = heappop(heap_road)
        while not unchecked[indeks]:
            m, indeks = heappop(heap_road)
        unchecked[indeks] = 0
        minimum_road[indeks] = Inf
        maxi = max(maxi, m)
        for i in range(len(nm[indeks])):
            if unchecked[i]:
                if nm[indeks][i] < minimum_road[i]:
                    minimum_road[i] = nm[indeks][i]
                    heappush(heap_road,(nm[indeks][i],i))
        count += 1
    return maxi


lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst(n, neighbour_matrix))
