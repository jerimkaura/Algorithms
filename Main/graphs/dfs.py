graph = {
    "A": ["D", "C", "B"],
    "B": ["E"],
    "C": ["G", "F"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"]
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

print(dfs_iteration(graph,"A"))