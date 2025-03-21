# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import array_list as lst
import priority_queue as pqueue
import dictionary as dct


class WeightedGraph:
    """
    A collection of vertices and weighted edges
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0

    def __eq__(self, other):
        return (type(other) == WeightedGraph
                and self.matrix == other.matrix
                and self.size == other.size)

    def __repr__(self):
        return "WeightedGraph(%r, %d)" % (self.matrix, self.size)


def order(graph):
    """
    Calculate the order of a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A WeightedGraph
    :return: The number of vertices in the graph
    """
    return dct.size(graph.matrix)


def size(graph):
    """
    Calculate the size of a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A WeightedGraph
    :return: The number of edges in the graph
    """
    return graph.size


def add_vertex(graph, vertex):
    """
    Add a vertex to a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A WeightedGraph
    :param vertex: An identifier of a vertex to be added
    :raise KeyError: If the vertex is already in the graph
    """
    if dct.get(graph.matrix, vertex) is not None:
        raise (KeyError)

    new_vertex = dct.Dictionary()
    dct.insert(graph.matrix, vertex, new_vertex)


def add_edge(graph, vertex_u, vertex_v, weight):
    """
    Add an edge, or reweight if one exists, to connect two vertices in a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A WeightedGraph
    :param vertex_u: An identifier of a vertex to be connected
    :param vertex_v: An identifier of a vertex to be connected
    :param weight: A weight of a connecting edge
    :raise KeyError: If either vertex is not in the graph
    :raise ValueError: If the weight is non-positive
    """
    adj_u = dct.get(graph.matrix, vertex_u)
    adj_v = dct.get(graph.matrix, vertex_v)

    if adj_u is None or adj_v is None:
        raise (KeyError)

    if weight < 0:
        raise(ValueError)

    if dct.get(adj_u, vertex_v) is None:
        dct.insert(adj_v, vertex_u, weight)
        dct.insert(adj_u, vertex_v, weight)
        graph.size += 1
    if dct.get(adj_u, vertex_v) != weight:
        dct.insert(adj_v, vertex_u, weight)
        dct.insert(adj_u, vertex_v, weight)


def remove_vertex(graph, vertex):
    """
    Remove a vertex from a graph.
    TODO: Implement this function. It may have up to O(n) complexity.

    :param graph: A WeightedGraph
    :param vertex: An identifier of a vertex to be removed
    :raise KeyError: If the vertex is not in the graph
    """
    vertex_adj = dct.get(graph.matrix, vertex)

    if vertex_adj is None:
        raise (KeyError)

    vertex_adj_list = dct.keys(vertex_adj)

    for i in range(0, dct.size(vertex_adj_list)):
        element = lst.get(vertex_adj_list, i)
        remove_edge(graph, vertex, element)

    dct.remove(graph.matrix, vertex)


def remove_edge(graph, vertex_u, vertex_v):
    """
    Remove an edge, if one exists, to disconnect two vertices in a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A WeightedGraph
    :param vertex_u: An identifier of a vertex to be connected
    :param vertex_v: An identifier of a vertex to be connected
    :raise KeyError: If either vertex is not in the graph
    """
    adj_u = dct.get(graph.matrix, vertex_u)
    adj_v = dct.get(graph.matrix, vertex_v)

    if adj_u is None or adj_v is None:
        raise (KeyError)

    if dct.get(adj_u, vertex_v) is not None:
        dct.remove(adj_v, vertex_u, 1)
        dct.remove(adj_u, vertex_v, 1)
        graph.size -= 1


def path(graph, vertex_u, vertex_v):
    """
    Find the shortest path between two vertices.
    TODO: Implement this function. It may have up to O(n^2 log n) complexity.

    :param graph: A WeightedGraph
    :param vertex_u: An identifier of a vertex at which to start
    :param vertex_v: An identifier of a vertex at which to end
    :return: A new List of vertices forming a path between the vertices
    :raise KeyError: If either vertex is not in the graph
    :raise ValueError: If there is no path between the vertices in the graph
    """
    # If edges have weight a path traversing fewer edges is not necessarily a path of less weight
    # Vertices to be explored must instead be stored in a priority queue, prioritized by distance
    # Things in the queue will be a tuple, where the first item is the distance and the second
    #   the vertex you want to go to
    adj_u = dct.get(graph.matrix, vertex_u)
    adj_v = dct.get(graph.matrix, vertex_v)

    if adj_u is None or adj_v is None:
        raise (KeyError)

    new_queue = pqueue.PriorityQueue()
    new_tuple = (0, vertex_u)
    pqueue.enqueue(new_queue, new_tuple)

    predecessor_dictionary = dct.Dictionary()
    dct.insert(predecessor_dictionary, vertex_u, vertex_u)

    distance_dictionary = dct.Dictionary()
    dct.insert(distance_dictionary, vertex_u, 0)

    while pqueue.size(new_queue) > 0:
        current_vertex = pqueue.dequeue(new_queue)
        vertex_dictionary = dct.get(graph.matrix, current_vertex[1])
        vertex_adj_list = dct.keys(vertex_dictionary)
        if current_vertex[1] == vertex_v:
            current_vertex_identifier = current_vertex[1]
            short_path = lst.List()
            while current_vertex_identifier is not vertex_u:
                lst.add(short_path, 0, current_vertex_identifier)
                current_vertex_identifier = dct.get(predecessor_dictionary, current_vertex_identifier)
            lst.add(short_path, 0, vertex_u)
            return short_path
        for i in range(0, lst.size(vertex_adj_list)):
            exploring_vertex = lst.get(vertex_adj_list, i)
            current_vertex_distance = current_vertex[0] * -1
            exploring_distance = dct.get(vertex_dictionary, exploring_vertex)
            # Exploring node has never been visited
            if dct.get(predecessor_dictionary, exploring_vertex) is None:
                new_value = (current_vertex_distance + exploring_distance) * -1
                new_tuple = (new_value, exploring_vertex)
                pqueue.enqueue(new_queue, new_tuple)
                dct.insert(predecessor_dictionary, exploring_vertex, current_vertex[1])
                dct.insert(distance_dictionary, exploring_vertex, (new_value * -1))
            # Exploring node has been visited
            if dct.get(predecessor_dictionary, exploring_vertex) is not None:
                exploring_vertex_old_distance = dct.get(distance_dictionary, exploring_vertex)
                exploring_distance = dct.get(vertex_dictionary, exploring_vertex)
                if exploring_distance + (current_vertex[0] * -1) < exploring_vertex_old_distance:
                    new_value = (exploring_distance + (current_vertex[0] * -1)) * -1
                    updated_tuple = (new_value, exploring_vertex)
                    pqueue.enqueue(new_queue, updated_tuple)
                    dct.insert(predecessor_dictionary, exploring_vertex, current_vertex[1])
                    dct.insert(distance_dictionary, exploring_vertex, (new_value * -1))
    raise (ValueError)


def length(graph, path):
    """
    Find the weighted length of a path.
    TODO: Implement this function. It may have up to O(m) complexity.

    :param graph: A WeightedGraph
    :param path: A non-empty List of vertices forming a path
    :return: The sum total weight of the path
    :raise KeyError: If any vertex or edge along the path is not in the graph
    """
    pointer = lst.size(path) - 1
    path_weight = 0

    while pointer > 0:
        current_vertex = lst.get(path, pointer)
        if dct.get(graph.matrix, current_vertex) is None:
            raise(KeyError)
        next_vertex = lst.get(path, pointer - 1)
        if dct.get(graph.matrix, next_vertex) is None:
            raise(KeyError)
        current_vertex_dictionary = dct.get(graph.matrix, current_vertex)
        distance_to_next = dct.get(current_vertex_dictionary, next_vertex)
        if distance_to_next is None:
            raise(KeyError)
        path_weight = path_weight + distance_to_next
        pointer -= 1

    return path_weight

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
