# Simple topological sort implementation using Depth-First Search(DFS)
# and Breadth-First Search(BFS) algorithms.

from collections import defaultdict, deque
from time import time

class Graph:
    def __init__(self, vertices):
        """
        Initialize a graph object.

        Parameters:
        - vertices (int): The number of vertices in the graph.
        """
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        """
        Add an edge to the graph.

        Parameters:
        - u (int): The source vertex of the edge.
        - v (int): The destination vertex of the edge.
        """
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        """
        A recursive utility function to perform topological sorting of the graph.
        Performs Depth-First Search(DFS) on the graph.

        Parameters:
        - v (int): The current vertex being visited.
        - visited (list): A list to keep track of visited vertices.
        - stack (list): A stack to store the topological order of the vertices.
        """
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        """
        Perform topological sorting of the graph.
        """
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack

    def topologicalSortBFS(self):
        in_degree = {i: 0 for i in range(self.V)}
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in self.graph if in_degree[node] == 0])
        topo_order = []

        while queue:
            current_node = queue.popleft()
            topo_order.append(current_node)
            for neighbor in self.graph[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != self.V:
            return []
        return topo_order

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Topological Sort using DFS of the given graph:")
start_time = time()
print(g.topologicalSort())
end_time = time()
print(f"Execution time: {end_time - start_time} seconds")

print("Topological Sort using BFS of the given graph:")
start_time = time()
print(g.topologicalSortBFS())
end_time = time()
print(f"Execution time: {end_time - start_time} seconds")
