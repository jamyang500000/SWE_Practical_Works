from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(f'{neighbor}({weight})' for neighbor, weight in self.graph[vertex])}")

    def bfs_shortest_path(self, start_vertex, end_vertex):
        visited = {start_vertex}
        queue = deque([(start_vertex, [start_vertex])]

        while queue:
            vertex, path = queue.popleft()
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    if neighbor == end_vertex:
                        return new_path
                    queue.append((neighbor, new_path))
        return None  # No path found

    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif parent != neighbor:
                    return True
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

    def is_bipartite(self):
        color = {}
        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0
                while queue:
                    current = queue.popleft()
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

# Example usage
g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 1)

print("Graph representation:")
g.print_graph()

# Test shortest path
print("\nShortest path from 0 to 3:", g.bfs_shortest_path(0, 3))

# Test cycle detection
print("Does the graph have a cycle?", g.has_cycle())

# Test Dijkstra's algorithm
g.add_edge(1, 3, 2)  # Adding weights to create a weighted graph
print("Shortest distances from vertex 0:", g.dijkstra(0))

# Test if the graph is bipartite
print("Is the graph bipartite?", g.is_bipartite())
