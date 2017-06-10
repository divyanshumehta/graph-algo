from collections import defaultdict

class Graph():

    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUntill(self, v, visited):
        visited[v] = True
        # print v
        for child in self.graph[v]:
            if visited[child] == False:
                self.DFSUntill(child,visited)

    def findMother(self):
        #store last element in complete DFS
        visited = [False] * self.V
        v=0
        for node in range(self.V):
            if visited[node] == False:
                self.DFSUntill(node,visited)
                v=node

        # now do DFS startinf at v and if all nodes visited then it is mother
        visited = [False] * self.V
        self.DFSUntill(v,visited)
        for i in range( len(visited) ):
            if visited[i] == False:
                return -1
        return v
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print "A mother vertex is " + str(g.findMother())
