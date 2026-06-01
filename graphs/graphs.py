'''graph: A graph is a collection of nodes (vertices) connected by edges.
Graphs can be directed or undirected, and they can be weighted or unweighted.
Graphs are used to model relationships between entities, such as social networks, transportation networks, and computer
networks.
Graph algorithms include:
1. Depth-First Search (DFS): A traversal algorithm that explores as far as possible along each branch before backtracking.
2. Breadth-First Search (BFS): A traversal algorithm that explores all the neighbors at the present depth before moving on to the nodes at the next depth level.
3. Dijkstra's Algorithm: An algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.
4. A* Search Algorithm: An algorithm that finds the shortest path between nodes in a graph, using heuristics to improve efficiency.
5. Topological Sort: An algorithm for ordering the vertices of a directed acyclic graph (DAG) in a linear sequence.
6. Prim's and Kruskal's Algorithms: Algorithms for finding the minimum spanning tree of a graph.
7. Bellman-Ford Algorithm: An algorithm for finding the shortest paths from a single source vertex to all other vertices in a graph, even with negative weight edges.
8. Floyd-Warshall Algorithm: An algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles).
9. Tarjan's Algorithm: An algorithm for finding strongly connected components in a directed graph.
10. Kosaraju's Algorithm: Another algorithm for finding strongly connected components in a directed graph.
graph diagrams:
1. Undirected Graph:
   A -- B
   |    |
   C -- D
   2. Directed Graph:
   A --> B
   |     |
   C --> D
   3. Weighted Graph: with 5edges
   A --(2)--> B
   |          |
   (3)        (4)     
   |          |
   C --(5)--> D'''

# creating a graph /vertex create / edges connecting
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, e , v ):
        self.graph.setdefault(e, []).append(v)
        self.graph.setdefault(v, []).append(e)
     # for undirected graph
    def display(self):
        for Vertex in self.graph:
            print(f"{Vertex} --> {self.graph[Vertex]}")

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.display()
