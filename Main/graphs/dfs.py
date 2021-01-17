graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

#DFS using iteration
#We will use a stack and a list to keep track of the visited nodes.
def dfs_iteration(graph, start_node):
    if start_node is None or start_node not in graph:
        return "Invalid"
    graph_path = []
    stack = [start_node]
    while len(stack) != 0:
        n = stack.pop()    
        if n not in graph_path:
            graph_path.append(n)        
        if n not in graph:
            continue
        for neighbor in graph[n]:
            stack.append(neighbor)    
    return graph_path

#DFS using a recursive method
def dfs_recursion(graph, start_node, graph_path=[]):
    if start_node not in graph_path:
        graph_path.append(start_node)
        if start_node not in graph:
            return graph_path
        for neighbor in graph[start_node]:
            dfs_recursion(graph,neighbor, graph_path)
    return graph_path

print(dfs_iteration(graph, "A"))
print(dfs_recursion(graph, "A"))
