import os

from decorators import measure_time
from filepaths import DATASET_PATH
from graph_parser import GraphParser
from sample_graph_generator import generate_graph


class GraphConnectivityChecker:
    def __init__(self, graph):
        self.graph = graph

    @measure_time
    def dfs(self, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_connected(self):
        if not self.graph:
            return True

        # Initialize visited flags
        visited = {node: False for node in self.graph}

        # Perform DFS from an arbitrary node
        start_node = next(iter(self.graph))
        self.dfs(start_node, visited)

        # Check if all nodes were visited
        return all(visited.values())


if __name__ == '__main__':
    # dataset_folder_path = input('Enter path to graph files folder: ') or DATASET_PATH
    # files_path = input('Enter name of graph files: ') or 'bay'
    # folder_path = os.path.join(dataset_folder_path, files_path)
    #
    # parser = GraphParser()
    # graph = parser.parse(folder_path)
    #
    # total_edges = sum(len(adjacent_vertices) for adjacent_vertices in graph['distance_edges'].values())
    # print('number of nodes: ', len(graph['distance_edges']), ', number of edges: ', total_edges)
    # print(graph['distance_edges'])

    graph = generate_graph(20, 15)
    print("generated graph: ", graph)

    connectivity_checker = GraphConnectivityChecker(graph)
    connected = connectivity_checker.is_connected()
    if connected:
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
