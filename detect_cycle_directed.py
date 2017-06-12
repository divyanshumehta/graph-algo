from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUntill(self, v, visited, ancestor):
        visited[v] = True
        ancestor[v] = True
        for child in self.graph[v]:
            if visited[child] == False:
                if self.DFSUntill(child,visited,ancestor) == 1:
                    return 1
            elif ancestor[child] == True:
                return 1
        ancestor[v] = False
        return 0

    def checkCycle(self):
        visited = [False] * self.V
        ancestor = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.DFSUntill(node,visited,ancestor) == 1:
                    return 1
        return 0

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.checkCycle() == 1:
    print "Graph has a cycle"
else:
    print "Graph has no cycle"
