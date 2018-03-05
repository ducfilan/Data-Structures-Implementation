class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.predecessor = None
        self.color = 'white'
        self.vertices_connected_to = {}

    def set_predecessor_vertex(self, v):
        self.predecessor = v

    def set_color(self, color):
        self.color = color

    def add_neighbor(self, v, cost=0):
        self.vertices_connected_to[v] = cost
