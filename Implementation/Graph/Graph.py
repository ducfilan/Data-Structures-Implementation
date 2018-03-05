from Implementation.Graph.Vertex import Vertex

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0

    def __len__(self):
        return len(self.vertices)

    def add_vertex(self, key):
        self.vertices_count += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        return self.vertices[key] if key in self.vertices else None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_key, to_key, cost=0):
        if from_key not in self.vertices:
            self.add_vertex(from_key)

        if to_key not in self.vertices:
            self.add_vertex(to_key)

        self.vertices[from_key].add_neighbor(to_key, cost)