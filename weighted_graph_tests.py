import unittest
from array_list import size as lsize, get as lget, set as lset
from dictionary import size as dsize, get as dget
from weighted_graph import *


class TestWeightedGraph(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing weighted graph equality and representation"

        graph = WeightedGraph()

        self.assertEqual(graph, graph, msg)
        self.assertEqual(repr(graph),
         "WeightedGraph(%r, 0)" % graph.matrix, msg)

    def test02_add(self):
        msg = "Testing adding vertices and edges to weighted graphs"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 3)
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1", 6)
        add_edge(graph, "v0", "v2", 2)
        add_edge(graph, "v0", "v3", 1)
        add_edge(graph, "v2", "v3", 8)

        self.assertEqual(order(graph), 4, msg)
        self.assertEqual(size(graph), 5, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v0")), 3, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v1"), 6, msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v2"), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v3"), 1, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v1")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v0"), 6, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v3"), 3, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v2")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v2"), "v0"), 2, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v2"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v2"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v2"), "v3"), 8, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v3")), 3, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v0"), 1, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v1"), 3, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v2"), 8, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v3"), msg)

    def test03_remove(self):
        msg = "Testing removing vertices and edges from weighted graphs"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 3)
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1", 6)
        add_edge(graph, "v0", "v2", 2)
        add_edge(graph, "v0", "v3", 1)
        add_edge(graph, "v2", "v3", 8)
        remove_vertex(graph, "v2")
        remove_edge(graph, "v3", "v0")

        self.assertEqual(order(graph), 3, msg)
        self.assertEqual(size(graph), 2, msg)
        self.assertIsNone(dget(graph.matrix, "v2"), msg)

        self.assertEqual(dsize(dget(graph.matrix, "v0")), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v1"), 6, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v2"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v3"), msg)

        self.assertEqual(dsize(dget(graph.matrix, "v1")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v0"), 6, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v3"), 3, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v3")), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v1"), 3, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v2"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v3"), msg)

    def test04_path(self):
        msg = "Testing finding shortest paths in weighted graphs"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 3)
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1", 6)
        add_edge(graph, "v0", "v2", 2)
        add_edge(graph, "v0", "v3", 1)
        add_edge(graph, "v2", "v3", 8)
        lst = path(graph, "v2", "v1")

        self.assertEqual(lsize(lst), 4, msg)
        self.assertEqual(lget(lst, 0), "v2", msg)
        self.assertEqual(lget(lst, 1), "v0", msg)
        self.assertEqual(lget(lst, 2), "v3", msg)
        self.assertEqual(lget(lst, 3), "v1", msg)
        self.assertEqual(length(graph, lst), 6, msg)

    def test05_add(self):
        msg = "Testing error cases"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 1)
        add_edge(graph, "v3", "v1", 1)
        add_edge(graph, "v1", "v3", 1)
        add_edge(graph, "v1", "v3", 1)
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_edge(graph, "v4", "v5", 1)
        remove_edge(graph, "v4", "v1")

        self.assertEqual(order(graph), 4, msg)
        self.assertEqual(size(graph), 2, msg)

    def test06_add(self):
        msg = "Testing error cases"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 1)
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1", 1)
        add_edge(graph, "v0", "v2", 1)
        add_edge(graph, "v0", "v3", 1)
        add_edge(graph, "v2", "v3", 1)
        add_vertex(graph, "v4")

        self.assertEqual(order(graph), 5, msg)
        self.assertEqual(size(graph), 5, msg)

        with self.assertRaises(KeyError): (add_edge(graph, "v1", "v7", 1), msg)
        with self.assertRaises(KeyError): (add_vertex(graph, "v3"), msg)
        with self.assertRaises(KeyError): (remove_vertex(graph, "v6"), msg)
        with self.assertRaises(KeyError): (remove_edge(graph, "v1", "v7"), msg)
        with self.assertRaises(KeyError): (path(graph, "v7", "v1"), msg)
        with self.assertRaises(ValueError): (path(graph, "v1", "v4"), msg)
        with self.assertRaises(ValueError): (add_edge(graph, "v2", "v4", -1), msg)

    def test07_path(self):
        msg = "Testing finding shortest paths in large weighted graphs"
        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")
        add_vertex(graph, "v3")
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_vertex(graph, "v6")
        add_edge(graph, "v1", "v2", 5)
        add_edge(graph, "v1", "v6", 45)
        add_edge(graph, "v1", "v5", 16)
        add_edge(graph, "v2", "v4", 44)
        add_edge(graph, "v2", "v3", 12)
        add_edge(graph, "v2", "v6", 43)
        add_edge(graph, "v3", "v5", 22)
        add_edge(graph, "v3", "v6", 38)
        add_edge(graph, "v4", "v5", 66)
        add_edge(graph, "v4", "v6", 69)
        lst = path(graph, "v2", "v5")

        self.assertEqual(lsize(lst), 3, msg)
        self.assertEqual(lget(lst, 0), "v2", msg)
        self.assertEqual(lget(lst, 1), "v1", msg)
        self.assertEqual(lget(lst, 2), "v5", msg)
        self.assertEqual(length(graph, lst), 21, msg)

    def test08_path(self):
        msg = "Testing finding shortest paths in large weighted graphs"
        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")
        add_vertex(graph, "v3")
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_vertex(graph, "v6")
        add_vertex(graph, "v7")
        add_vertex(graph, "v8")
        add_vertex(graph, "v9")
        add_vertex(graph, "v10")
        add_vertex(graph, "v11")
        add_vertex(graph, "v12")
        add_vertex(graph, "v13")
        add_edge(graph, "v1", "v2", 5)
        add_edge(graph, "v1", "v6", 45)
        add_edge(graph, "v1", "v5", 16)
        add_edge(graph, "v2", "v4", 44)
        add_edge(graph, "v2", "v3", 12)
        add_edge(graph, "v2", "v6", 43)
        add_edge(graph, "v3", "v5", 22)
        add_edge(graph, "v3", "v6", 38)
        add_edge(graph, "v3", "v12", 8)
        add_edge(graph, "v4", "v5", 66)
        add_edge(graph, "v4", "v6", 69)
        add_edge(graph, "v5", "v10", 8)
        add_edge(graph, "v6", "v12", 18)
        add_edge(graph, "v7", "v8", 16)
        add_edge(graph, "v7", "v10", 41)
        add_edge(graph, "v7", "v12", 58)
        add_edge(graph, "v7", "v13", 64)
        add_edge(graph, "v8", "v9", 23)
        add_edge(graph, "v8", "v13", 37)
        add_edge(graph, "v9", "v12", 35)
        add_edge(graph, "v9", "v13", 48)
        add_edge(graph, "v10", "v13", 45)
        add_edge(graph, "v10", "v11", 9)
        add_edge(graph, "v12", "v13", 68)
        lst = path(graph, "v1", "v8")

        self.assertEqual(lsize(lst), 5, msg)
        self.assertEqual(lget(lst, 0), "v1", msg)
        self.assertEqual(lget(lst, 1), "v5", msg)
        self.assertEqual(lget(lst, 2), "v10", msg)
        self.assertEqual(lget(lst, 3), "v7", msg)
        self.assertEqual(lget(lst, 4), "v8", msg)
        self.assertEqual(length(graph, lst), 81, msg)

    def test09_length(self):
        msg = "Testing length error cases"
        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")
        add_vertex(graph, "v3")
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_vertex(graph, "v6")
        add_edge(graph, "v1", "v2", 5)
        add_edge(graph, "v1", "v6", 45)
        add_edge(graph, "v1", "v5", 16)
        add_edge(graph, "v2", "v4", 44)
        add_edge(graph, "v2", "v3", 12)
        add_edge(graph, "v2", "v6", 43)
        add_edge(graph, "v3", "v5", 22)
        add_edge(graph, "v3", "v6", 38)
        add_edge(graph, "v4", "v5", 66)
        add_edge(graph, "v4", "v6", 69)
        lst = path(graph, "v2", "v5")
        remove_edge(graph, "v1", "v5")
        lset(lst, 0, "v100")

        self.assertEqual(lsize(lst), 3, msg)
        with self.assertRaises(KeyError): (length(graph, lst), msg)

    def test10_length(self):
        msg = "Testing length error cases"
        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")
        add_vertex(graph, "v3")
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_vertex(graph, "v6")
        add_edge(graph, "v1", "v2", 5)
        add_edge(graph, "v1", "v6", 45)
        add_edge(graph, "v1", "v5", 16)
        add_edge(graph, "v2", "v4", 44)
        add_edge(graph, "v2", "v3", 12)
        add_edge(graph, "v2", "v6", 43)
        add_edge(graph, "v3", "v5", 22)
        add_edge(graph, "v3", "v6", 38)
        add_edge(graph, "v4", "v5", 66)
        add_edge(graph, "v4", "v6", 69)
        lst = path(graph, "v2", "v5")
        lset(lst, 1, "v7")

        self.assertEqual(lsize(lst), 3, msg)
        with self.assertRaises(KeyError): (length(graph, lst), msg)

    def test11_length(self):
        msg = "Testing length error cases"
        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")
        add_vertex(graph, "v3")
        add_vertex(graph, "v4")
        add_vertex(graph, "v5")
        add_vertex(graph, "v6")
        add_edge(graph, "v1", "v2", 5)
        add_edge(graph, "v1", "v6", 45)
        add_edge(graph, "v1", "v5", 16)
        add_edge(graph, "v2", "v4", 44)
        add_edge(graph, "v2", "v3", 12)
        add_edge(graph, "v2", "v6", 43)
        add_edge(graph, "v3", "v5", 22)
        add_edge(graph, "v3", "v6", 38)
        add_edge(graph, "v4", "v5", 66)
        add_edge(graph, "v4", "v6", 69)
        lst = path(graph, "v2", "v5")
        lset(lst, 2, "v7")

        self.assertEqual(lsize(lst), 3, msg)
        with self.assertRaises(KeyError): (length(graph, lst), msg)

    def test12_add(self):
        msg = "Testing error cases"

        graph = WeightedGraph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3", 2)
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_vertex(graph, "v4")
        add_edge(graph, "v3", "v1", 3)

        self.assertEqual(order(graph), 5, msg)
        self.assertEqual(size(graph), 1, msg)

        self.assertEqual(dget(dget(graph.matrix, "v1"), "v3"), 3, msg)

if __name__ == "__main__":
    unittest.main()
