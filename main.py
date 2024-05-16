import os

from decorators import measure_time
from filepaths import DATASET_PATH
from graph_parser import GraphParser
from sample_graph_generator import generate_graph


class GraphConnectivityChecker:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    @measure_time
    def find_connected_components(self):
        visited = {node: False for node in self.graph}
        connected_components = []
        for node in self.graph:
            if not visited[node]:
                component = []
                self.dfs(node, visited, component)
                connected_components.append(component)
        return connected_components

    @measure_time
    def is_connected(self):
        if not self.graph:
            return True
        visited = {node: False for node in self.graph}
        start_node = next(iter(self.graph))
        self.dfs(start_node, visited, [])
        return all(visited.values())


if __name__ == '__main__':
    # dataset_folder_path = input('Enter path to graph files folder: ') or DATASET_PATH
    # files_path = input('Enter name of graph files: ') or 'bay'
    # folder_path = os.path.join(dataset_folder_path, files_path)
    #
    # parser = GraphParser()
    # parsed_graph = parser.parse(folder_path)
    # graph = parsed_graph['distance_edges']
    #
    # total_edges = sum(len(adjacent_vertices) for adjacent_vertices in graph.values())
    # print('number of nodes: ', len(graph), ', number of edges: ', total_edges)
    # print(graph['distance_edges'])

    graph = generate_graph(20, 95)
    print("generated graph: ", graph)

    connectivity_checker = GraphConnectivityChecker(graph)
    connected = connectivity_checker.is_connected()
    if connected:
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
        connected_components = connectivity_checker.find_connected_components()
        print("Connected components:")
        for i, component in enumerate(connected_components, start=1):
            print(f"Component {i}: {component}")
