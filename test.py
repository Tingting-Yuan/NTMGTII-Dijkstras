import unittest
from dijkstra import Graph

class Graph_Test(unittest.TestCase):
    
    #Runs before each test
    def setUp(self):
        self.graph = Graph()
        self.graph2 = Graph()

        # Graph 1
        self.graph.add_vertex('A', {'B': 7, 'C': 8})
        self.graph.add_vertex('B', {'A': 7, 'F': 2})
        self.graph.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
        self.graph.add_vertex('D', {'F': 8})
        self.graph.add_vertex('E', {'H': 1})
        self.graph.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
        self.graph.add_vertex('G', {'C': 4, 'F': 9})
        self.graph.add_vertex('H', {'E': 1, 'F': 3})

        # Graph 2
        self.graph2.add_vertex('X', {'Y': 5, 'Z': 2})
        self.graph2.add_vertex('Y', {'X': 5, 'Z': 1, 'W': 7})
        self.graph2.add_vertex('Z', {'X': 2, 'Y': 1, 'W': 4})
        self.graph2.add_vertex('W', {'Y': 7, 'Z': 4})

    def test_add_vertex(self):
        g = Graph()
        g.add_vertex('A', {'B': 7, 'C': 8})
        self.assertEqual(g.vertices, {'A': {'C': 8, 'B': 7}})
        
    def test_shortest_path_graph1(self):
        self.assertEqual(self.graph.shortest_path('A', 'H'), ['H', 'F', 'B'])
        self.assertEqual(self.graph.shortest_path('H', 'I'), {'A': 12, 'B': 5, 'C': 9, 'D': 11, 'E': 1, 'F': 3, 'G': 12, 'H': 0})

    def test_shortest_path_graph2(self):
        # Graph2
        self.assertEqual(self.graph2.shortest_path('X', 'W'), ['W', 'Z'])
        self.assertEqual(self.graph2.shortest_path('Y', 'Z'), ['Z'])
        self.assertEqual(self.graph2.shortest_path('Z', 'W'), ['W'])
        self.assertEqual(self.graph2.shortest_path('W', 'X'), ['X', 'Z'])

    def test_nonexistent_node(self):
        # Test node not in graph
        self.assertTrue(self.graph.shortest_path('A', 'Z') in [None, []])

if __name__ == "__main__":
    unittest.main()
