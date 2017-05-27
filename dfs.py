from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUntil(self, node, visited):
        visited[node] = True
        print node
        for child in self.graph[node]:
            if visited[child] == False:
                self.DFSUntil(child,visited)

    def DFS(self):
        visited = [False] * len(self.graph)
        for start in range( len(self.graph) ):
            if visited[start] == False:
                self.DFSUntil(start, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print "Following the is DFS"
g.DFS()
