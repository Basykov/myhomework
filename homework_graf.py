class Graph:
    def __init__(self):
        self.graph = {}

    def add_top(self, top):
        if top not in self.graph:
            self.graph[top] = []

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.add_top(source)
        if destination not in self.graph:
            self.add_top(destination)
        self.graph[source].append((destination, weight))

    def print_graph(self):
        for top in self.graph:
            print(f"Вершина {top}: ", end="")
            for edge in self.graph[top]:
                print(f"({edge[0]}, Номер: {edge[1]})", end=" ")
            print()


g = Graph()
g.add_edge('FF', 'GH', 3)
g.add_edge('FF', 'CR', 2)
g.add_edge('GH', 'CR', 5)
g.add_edge('CR', 'DD', 1)

g.print_graph()