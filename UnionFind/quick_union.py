'''
uses he same data structure as quick find
in this configuration , each array element's value points to it's 'parent'
if the value of the node is the same as its index we call it a root, in other
words it has no parent nodes.

quick union is faster than quick find in most cases but if the tree is really tall
we will get N
'''
from quick_find import  QuickFind
class QuickUnion(QuickFind):
    # def __init__(self ,array_size , array = []):
        # super().__init__(array_size , array = [])
    def get_root(self , node_index):
        while node_index != self.array[node_index]:
            node_index = self.array[node_index]
        return node_index
    def is_conneced(self , node_1_index, node_2_index):
        return self.get_root(node_1_index) == self.get_root(node_2_index)
    def union(self, node_1_index , node_2_index):
        root1 = self.get_root(node_1_index)
        root2 = self.get_root(node_2_index)
        if root1 == root2:
            return 0
        else:
            self.array[root2] = root1
        return 0
