from collections import deque

class GraphUsingAdjacencyMatrix:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.Vertices = [None] * numVertices
        self.AdjacencyMat = [[0] * numVertices for _ in range(numVertices)]

    def addVertex(self, index, vertex):
        if 0 <= index < self.numVertices:
            if vertex not in self.Vertices:
                self.Vertices.append(vertex)
            else:
                print(f"vertex {vertex} is already present")
        else:
            print("index is out of bound")

    def addEdge(self, source, destination, weight = 1):         #here source and destination are indeces
        if (0 <= source < self.numVertices) and (0 <= destination < self.numVertices):
            self.AdjacencyMat[source][destination] = weight
            self.AdjacencyMat[destination][source] = weight
        else:
            print("one or both idices are out of bound...")

    def display(self):
        for index, vertex in enumerate(self.Vertices):
            if vertex is not None:
                print(f"Index: {index}, Vertex: {vertex}")

        for row in self.AdjacencyMat:
            print(row)

    def dfs(self, startVertex = 0):
        dfsResult = []
        visited = [False] * self.numVertices
        return self.dfsRecursive(startVertex, dfsResult, visited)
    
    def dfsRecursive(self, vertex, dfsResult, visited):
        dfsResult.append(vertex)
        visited[vertex] = True

        for neighbor in range(self.numVertices):
            if neighbor == vertex:
                continue

            if self.AdjacencyMat[vertex][neighbor] == 1:
                if visited[neighbor] == False:
                    self.dfsRecursive(neighbor, dfsResult, visited)
        return dfsResult        #returns when all the traversal done
    
    def bfs(self, startVertex = 0):
        bfsResult = []
        visited = [False] * self.numVertices
        queue = deque([startVertex])
        visited[startVertex] = True

        while queue:
            vertex = queue.popleft()
            bfsResult.append(vertex)
            for neighbor in range(self.numVertices):
                if self.AdjacencyMat[vertex][neighbor] != 0:
                    if visited[neighbor] == False:
                        queue.append(neighbor)
                        visited[neighbor] = True
        return bfsResult






graph = GraphUsingAdjacencyMatrix(7)

#Add vertices
graph.addVertex(0, 'A')
graph.addVertex(1, 'B')
graph.addVertex(2, 'C')
graph.addVertex(3, 'D')
graph.addVertex(4, 'E')
graph.addVertex(5, 'F')
graph.addVertex(6, 'G')

#Add edges
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.addEdge(2, 4)
graph.addEdge(0, 5)
graph.addEdge(5, 6)

print(graph.bfs())
