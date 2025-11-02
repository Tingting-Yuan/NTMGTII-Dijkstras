import unittest
from dijkstra import Graph

class Graph_Test(unittest.TestCase):
    def setUp(self):
        """Prepare a sample graph for all tests."""
        self.g = Graph()
        self.g.add_vertex('A', {'B': 7, 'C': 8})
        self.g.add_vertex('B', {'A': 7, 'F': 2})
        self.g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
        self.g.add_vertex('D', {'F': 8})
        self.g.add_vertex('E', {'H': 1})
        self.g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
        self.g.add_vertex('G', {'C': 4, 'F': 9})
        self.g.add_vertex('H', {'E': 1, 'F': 3})

    def test_shortest_path_A_to_H(self):
        """Check the main example path from A to H."""
        path = self.g.shortest_path('A', 'H')
        self.assertEqual(path, ['A', 'B', 'F', 'H'])

    def test_reverse_path_H_to_A(self):
        """Check that reverse direction produces correct path."""
        path = self.g.shortest_path('H', 'A')
        self.assertEqual(path, ['H', 'F', 'B', 'A'])

    def test_path_to_self(self):
        """Path from a node to itself should just be the node."""
        path = self.g.shortest_path('C', 'C')
        self.assertEqual(path, ['C'])

    def test_nonexistent_node(self):
        """Nonexistent node should return None."""
        path = self.g.shortest_path('A', 'Z')
        self.assertIsNone(path)

    def test_unreachable_node(self):
        """If node is unreachable, algorithm should return distance table."""
        # 'E' and 'H' form a disconnected subgraph (except through F)
        g2 = Graph()
        g2.add_vertex('A', {'B': 1})
        g2.add_vertex('B', {'A': 1})
        g2.add_vertex('C', {})  # disconnected node
        result = g2.shortest_path('A', 'C')
        self.assertIsInstance(result, dict)
        self.assertIn('A', result)
        self.assertIn('C', result)

if __name__ == '__main__':
    unittest.main()
