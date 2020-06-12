from collections import defaultdict
import copy

def add(graph, u, v):
    graph[u].append(v)
    if len(graph[v]) == 0:
        pass
    #graph[v].append(u)


def generate_edge(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for new_node in graph[start]:
        if new_node not in path:
            new_path = find_path(graph, new_node, end, path)
            if new_path:
                return new_path
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def find_shortest(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


def dfs_util(graph, vertex, visited):
    visited[vertex] = True
    print vertex
    for i in graph[vertex]:
        if not visited[i]:
            dfs_util(graph, i, visited)


def dfs_util_2(graph, vertex, visit):
    visit[vertex] = True
    #print vertex
    for i in graph[vertex]:
        if not visit[i]:
            dfs_util_2(graph, i, visit)
    return visit


def dfs(graph):
    #visited = {}
    #for i in graph:
    #    visited[i] = False
    for i in graph:
        #if not visited[i]:
            print 'Starting iteration for {}'.format(i)
            visited_nodes = dfs_util_2(graph, i, defaultdict(bool))
            #dfs_util(graph, i, visited)
            print 'Ending iteration for {}'.format(i)
            if len(visited_nodes) == len(graph):
                print '{} is mother vertex'.format(i)


def main():
    graph = defaultdict(list)
    #add(graph, 'a', 'a')
    #add(graph, 'a', 'b')
    #add(graph, 'b', 'c')
    #add(graph, 'a', 'c')
    #add(graph, 'c', 'b')
    #add(graph, 'd', 'f')
    #add(graph, 'd', 'g')
    add(graph, '0', '1')
    add(graph, '0', '2')
    add(graph, '1', '3')
    add(graph, '4', '1')
    add(graph, '5', '2')
    add(graph, '5', '6')
    add(graph, '6', '0')
    add(graph, '6', '4')
    dfs(graph)

    graph_2 = defaultdict(list)
    add(graph_2, '0', '2')
    add(graph_2, '0', '3')
    add(graph_2, '1', '0')
    add(graph_2, '2', '1')
    add(graph_2, '3', '4')
    dfs(graph_2)
    #print find_all_paths(graph, 'd', 'f')
    #print generate_edge(graph)
    #print find_path(graph, 'a', 'd')
    #print find_path(graph, 'b', 'd')
    #print find_all_paths(graph, 'a', 'd')
    #print find_all_paths(graph, 'b', 'd')
    #print find_all_paths(graph, 'a', 'c')
    #print find_shortest(graph, 'a', 'd')


main()
