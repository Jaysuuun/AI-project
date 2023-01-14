class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def put(self, item):
        self.items.append(item)
    def get(self):
        return self.items.pop(0)
graph = {
    'A': ['B', 'C','D'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F','G'],
    'D': ['B','E','F'],
    'E': ['B', 'D','F','G'],
    'F': ['C', 'E','D','G'],
    'G': ['E','F','B']
}

def bfs(graph, start, goal, blocked_nodes = []):
    queue = Queue()
    queue.put((start, [start]))
    while not queue.is_empty():
        node, path = queue.get()
        if node == goal:
            return path
        if node not in blocked_nodes:
            for neighbour in graph[node]:
                if neighbour not in path:
                    queue.put((neighbour, path + [neighbour]))
    return None

blocked_nodes = input("Enter a comma separated list of nodes to block (or press enter to search without blocking any node): ").split(",")
shortest_path = bfs(graph, 'A', 'G', blocked_nodes)
if shortest_path != None:
    print("Shortest path: ", shortest_path)
else:
    print("No path found")