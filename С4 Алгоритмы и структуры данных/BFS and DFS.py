graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}
 #BFS
visited = []
queue = []

visited1 = set() #DFS


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def dfs(visited1, graph, node):
    if node not in visited:
        print (node)
        visited1.add(node)
        for neighbor in graph[node]:
            dfs(visited1, graph, neighbor)