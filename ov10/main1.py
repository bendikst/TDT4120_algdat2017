from sys import stdin, stderr

def best_path(nm, prob, unvisited, end):
    visited = set()
    prob_distance = [0]*len(unvisited)
    predecessors = {}

    prob_distance[0] = prob[0]
    vertex = unvisited[0]
    while True:
        if vertex == end:
            break
        for neighbour in range(len(nm[vertex])):
            if neighbour not in visited:
                if nm[vertex][neighbour]:
                    new_prob = prob_distance[vertex] * prob[neighbour]
                    if new_prob > prob_distance[neighbour]:
                        prob_distance[neighbour] = new_prob
                        predecessors[neighbour] = vertex
        visited.add(vertex)
        unvisited.remove(vertex)

        temp_max = 0
        for v in unvisited:
            if prob_distance[v] > temp_max:
                temp_max = prob_distance[v]
                vertex = v
    if prob_distance[-1] == 0.0:
        return '0'

    result, v = str(end), end
    while v != 0:
        result += '-'
        result += str(predecessors[v])
        v = predecessors[v]
    return result[::-1]


n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
unvisited, node = [], 0
for line in stdin:
    unvisited.append(node)
    node += 1
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities, unvisited, n-1))
