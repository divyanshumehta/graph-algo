from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u, v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False] * len((self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            node = queue.pop(0)
            print node

            ##Enqueue adjacent nodes
            for child in self.graph[node]:
                if visited[child] == False:
                    queue.append(child)
                    visited[child] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

s = input("Enter starting edge")
g.BFS(s)
