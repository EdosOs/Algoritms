'''
nodes are considered connected if they have the same value
too slow, N unions for array of size N is potentially O(N^2).
'''
class QuickFind:
    def __init__(self ,array_size , array = []):
        self.array_size = array_size
        self.id_array = [i for i in range(array_size)]
        self.array = array if array != [] else self.id_array.copy()

    def is_conneced(self , node1_id, node2_id):
        return self.array[node1_id] == self.array[node2_id]


    def union(self , node1_id, node2_id):
        if self.is_conneced(node1_id , node2_id) == 1:
            return 0
        else:
            for node in self.array:
                if node == self.array[node2_id]:
                    node = self.array[node1_id]
        return 0