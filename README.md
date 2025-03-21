# Weighted-Graphs

CSC 202 Data Structures Weighted-Graphs Project

Function weighted_graph.path: Take as arguments, a weighted path and two vertices, then efficiently determine the shortest path between the given vertices. Maintain a priority queue of vertices to be explored, such that closer vertices are dequeued and explored first, leading to shorter paths. Returns the resulting shortest path as a list of vertices

Function weighted_graph.length: Take as arguments a weighted graph and a list of vertices representing a path, then efficiently determine the length of the given path. Considers only the vertices passed through and edges traversed by the given path, raising an error if any of them do not exist. Returns the sum total weight of the edges traversed by the given path
