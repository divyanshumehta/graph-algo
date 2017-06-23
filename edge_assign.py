from collections import defaultdict

class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.topo_sort = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self,v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        self.topo_sort = stack

    def addUndirectedEdge(self, u, v):

        for i in range(self.V):
            if self.topo_sort[i] == u:
                self.addEdge(u, v)
                print u,"->",v
                break

            if self.topo_sort[i] == v:
                self.addEdge(v, u)
                print v,"->",u
                break

# Driver program to check above functions
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 5)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.topologicalSort()
print "The Edge to avoid cycle are as follows"
g.addUndirectedEdge(0, 2)
g.addUndirectedEdge(0, 3)
g.addUndirectedEdge(4, 5)
