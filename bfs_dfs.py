from collections import deque, defaultdict
def input_graph():
    graph = defaultdict(list)
    n = int(input("Enter the number of edges: "))
    print("Enter the edges (format: from to)")
    for _ in range(n):
        u, v = input().split()
        graph[u].append(v)
    return graph

def bfs(graph, start):
    q = deque(start)
    visited = set()
    visited.add(start)
    print("bfs: ", end = " ")

    while q:
        node = q.popleft()
        print(node, end = " ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)

def dfs(graph, start):
    stack = [start]
    visited = set()
    print("\ndfs: ", end = " ")

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end = " ")
            visited.add(node)
            stack.extend(reversed(graph[node]))


if __name__ == "__main__":
    graph = input_graph()
    start = input("Enter start node: ")
    bfs(graph, start)
    dfs(graph, start)
    