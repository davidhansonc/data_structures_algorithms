# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-28 11:15:49
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-28 11:57:45
class Graph():

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}


    def add_vertex(self, node):
        if node not in self.adjacency_list:
            self.number_of_nodes += 1
            self.adjacency_list[node] = []
            return
        else:
            return "node already exists"


    def add_edge(self, node1, node2):
        try:
            if node2 not in self.adjacency_list[node1] and \
                    node1 not in self.adjacency_list[node2]:
                self.adjacency_list[node1].append(node2)
                self.adjacency_list[node2].append(node1)
                return
            else:
                return print("Edge already exists.")
        except KeyError:
            return print("Error: Node does not exist.")


    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.show_connections()
print(my_graph.adjacency_list)