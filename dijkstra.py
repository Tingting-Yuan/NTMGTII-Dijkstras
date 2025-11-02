import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        """Add a vertex and its edges to the graph."""
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        """Compute the shortest path using Dijkstra's algorithm."""
        # ✅ 如果起点或终点不存在，直接返回 None
        if start not in self.vertices or finish not in self.vertices:
            return None
        
        distances = {}
        previous = {}
        nodes = []

        for vertex in self.vertices:
            if vertex == start:
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:
                # ✅ 构造反向路径
                path = []
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                return path  # 保持测试期望 ['H','F','B']
            
            if distances[smallest] == sys.maxsize:
                break
            
            for neighbor in self.vertices[smallest]:
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        
        return distances  # 如果没找到路径，返回距离表
    
    def __str__(self):
        return str(self.vertices)


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    print(g.shortest_path('A', 'H'))  # 输出 ['H','F','B']
