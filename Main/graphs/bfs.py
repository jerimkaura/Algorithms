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

queue = []  
def bfs(graph, start_node):
	visited = [False] * len(graph)
	queue.append(start_node)
	while queue:
		s = queue.pop(0)
		print(s,"-->", end=" ")
		for neighbour in graph[s]:
			if neighbour not in visited:
				queue.append(neighbour)

bfs(graph, 'A')
