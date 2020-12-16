graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        print(f"Vertex {stack}")
        print(f"Vertex {vertex}")
        print(f"Visited {visited}")
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    print(visited)
    return visited

dfs(graph, 'A')
