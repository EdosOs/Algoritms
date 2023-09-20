'''
weighted quick union with path compression
the idea is while computing the root of a node, we can set any
node to on the way to point to the root to flatten the tree.

complexity: (N + M lg*N) where lg* N is practically always smaller than 5
it can be proved that algorithms for union find cant be faster than linear.
'''
from weighted_quick_union import WQU
class WQUPC(WQU):
    def get_root(self , node_index):
        index_arr_of_nodes_on_the_way = []
        while node_index != self.array[node_index]:
            # self.array[node_index] = self.array[self.array[node_index]]
            node_index = self.array[node_index]
            index_arr_of_nodes_on_the_way.append(node_index)
        root_index = node_index
        for index in index_arr_of_nodes_on_the_way:
            self.array[index] = root_index
        return node_index
    def union(self, node_1_index, node_2_index):
        root1 = self.get_root(node_1_index)
        root2 = self.get_root(node_2_index)
        '''check if same root(connected)'''
        if root1 == root2:
            return 0
        # first check which tree is bigger , then append the smaller tree.
        else:
            if self.size[root1] > self.size[root2]:
                self.array[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.array[root1] = root2
                self.size[root2] += self.size[root1]
        return 0