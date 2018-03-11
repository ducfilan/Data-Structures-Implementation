class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.predecessor = None
        self.color = 'white'
        self.vertices_connected_to = {}
        self.distance = 0

    def set_predecessor_vertex(self, v):
        self.predecessor = v

    def get_predecessor_vertex(self):
        return self.predecessor

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_cost(self, v):
        return self.vertices_connected_to[v]

    def add_neighbor(self, v, cost=0):
        self.vertices_connected_to[v] = cost

    def set_distance(self, d):
        self.distance = d
