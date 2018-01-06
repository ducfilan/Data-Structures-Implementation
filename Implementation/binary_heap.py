class BinaryHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]

            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)
