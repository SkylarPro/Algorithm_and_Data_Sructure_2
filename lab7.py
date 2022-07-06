import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visitied = []

    def bfs(self, node):
        self.visitied.append(node)
        queue = []
        queue.append(node)

        while queue:
            s = queue.pop()
            print(s, end=" ")
            for neigbord in self.graph[s]:
                if neigbord not in self.visitied:
                    self.visitied.append(neigbord)
                    queue.append(neigbord)
        self.visitied = []

    def dfs(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            for neigbord in self.graph[node]:
                self.dfs(neigbord, visited)

    def deikstra(self, strat_node):
        unvisited_nodes = list(self.graph)
        shortest_path, previous_nodes = {node: float('+inf') for node in unvisited_nodes}, {}
        shortest_path[strat_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = self.graph[current_min_node]
            for neighbor in neighbors:
                value = shortest_path[current_min_node] + self.graph[current_min_node][neighbor]
                if value < shortest_path[neighbor]:
                    shortest_path[neighbor] = value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path

    def kruskal(self):
        graph_kruskal = []
        for node in self.graph:
            for neigh in self.graph[node]:
                graph_kruskal.append((neigh, node, self.graph[node][neigh]))
        graph_kruskal.sort(key=lambda x: x[2])
        graph_kruskal = graph_kruskal[::2]
        union_node = set()
        isolate_node = {}
        ostrov_res = set()

        for connection in graph_kruskal:
            if connection[0] not in union_node or connection[1] not in union_node:
                if connection[0] not in union_node and connection[1] not in union_node:
                    isolate_node[connection[0]] = [connection[0], connection[1]]
                    isolate_node[connection[1]] = isolate_node[connection[0]]
                else:
                    if not isolate_node.get(connection[0]):
                        isolate_node[connection[1]].append(connection[0])
                        isolate_node[connection[0]] = isolate_node[connection[1]]
                    else:
                        isolate_node[connection[0]].append(connection[1])
                        isolate_node[connection[1]] = isolate_node[connection[0]]

                ostrov_res.add(connection)
                union_node.add(connection[0])
                union_node.add(connection[1])
        # return ostrov_res
        for connection in graph_kruskal:
            if connection[1] not in isolate_node[connection[0]]:
                ostrov_res.add(connection)
                bridge = isolate_node[connection[0]]
                isolate_node[connection[0]] += isolate_node[connection[1]]
                isolate_node[connection[1]] += bridge

        return ostrov_res

if __name__ == "__main__":
    graph = {
        'A': {'D': 3, 'B': 2, 'E': 5},
        'B': {'A': 2, 'C': 10},
        'C': {'B': 10, 'E': 2, 'H': 5, 'I': 6},
        'D': {'A': 3, 'F': 8},
        'E': {'A': 5, 'C': 2, 'F': 7},
        'F': {'D': 8, 'E': 7, 'H': 3, 'G': 4},
        'H': {'F': 3, 'C': 5},
        'G': {'F': 4, 'I': 11},
        'I': {'G': 11, 'C': 6},
    }
    gr = Graph(graph)
    print("BFS")
    gr.bfs('A')
    print("\nDFS")
    gr.dfs('A')
    previous_nodes, shortest_path = gr.deikstra('A')
    print("\nDeikstra previous:", previous_nodes)
    print("Deikstra path:", shortest_path)


    ostrov_res = gr.kruskal()
    graph = nx.Graph()
    print(ostrov_res)
    graph.add_weighted_edges_from(ostrov_res)
    nx.draw(graph,
                         node_color='red',
                         node_size=1000,
                         with_labels=True)
    plt.show()