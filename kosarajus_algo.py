from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def Transpose(self, vertices):
        g = Graph(vertices)
        for node in self.graph:
            for child in self.graph[node]:
                g.addEdge(child, node)
        return g

    def DFSUntill(self, v, visited):
        visited[v] = True
        print v
        for child in self.graph[v]:
            if visited[child] == False:
                self.DFSUntill(child,visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for child in self.graph[v]:
            if visited[child] == False:
                self.fillOrder(child, visited, stack)
        stack = stack.append(v)

    def printSCC(self):
        stack = []
        visited = [False] * self.V

        for node in range(self.V):
            if visited[node] == False:
                self.fillOrder(node, visited, stack)

        gr = self.Transpose(self.V)
        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUntill(i, visited)
                print " "

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)


print ("Following are strongly connected components " +
                           "in given graph")
g.printSCC()
