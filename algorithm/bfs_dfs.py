import sys


def get_graph():
    graph = dict()

    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    return graph


def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if graph.get(node) is not None:
                graph[node].sort(reverse=True)
                need_visit.extend(graph[node])
    return visited


def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            if graph.get(node) is not None:
                graph[node].sort()
                need_visit.extend(graph[node])
    return visited


def dfs_bfs_1260():
    input_val = list(map(int, sys.stdin.readline().split()))
    graph = dict()
    for idx in range(input_val[1]):
        graph_val = list(map(int, sys.stdin.readline().split()))
        if graph.get(graph_val[0]) is None:
            graph[graph_val[0]] = [graph_val[1]]
        else:
            graph[graph_val[0]].append(graph_val[1])
        if graph.get(graph_val[1]) is None:
            graph[graph_val[1]] = [graph_val[0]]
        else:
            graph[graph_val[1]].append(graph_val[0])
    sorted_graph = dict(sorted(graph.items()))
    bfs_arr = bfs(sorted_graph, input_val[2])
    dfs_arr = dfs(sorted_graph, input_val[2])
    sys.stdout.write(f"{' '.join(str(x) for x in dfs_arr)}\n")
    sys.stdout.write(f"{' '.join(str(y) for y in bfs_arr)}\n")


if __name__ == "__main__":
    # dfs(get_graph(), 'A')
    # bfs(get_graph(), 'A')
    dfs_bfs_1260()
