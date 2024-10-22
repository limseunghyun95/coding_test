import copy


def dfs(nodes, visited, m):
    if len(visited) == m:
        print(' '.join(map(str, visited)))
    for index, node in enumerate(nodes):
        if node == 0 and index != 0 and len(visited) < m:
            new_nodes = copy.deepcopy(nodes)
            new_nodes[index] = 1
            new_visited = copy.deepcopy(visited)
            new_visited.append(index)
            dfs(new_nodes, new_visited, m)


n, m = map(int, input().split())

for i in range(1, n + 1):
    nodes = [0] * (n + 1)
    nodes[i] = 1
    visited = [i]

    dfs(nodes, visited, m)
