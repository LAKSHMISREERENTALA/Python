# Define the graph
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Initialize visited list
visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Run DFS starting from node '5'
print("DFS traversal starting from node '5':")
dfs(visited, graph, '5')
