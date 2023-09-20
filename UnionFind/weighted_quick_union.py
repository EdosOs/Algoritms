'''
data structure : array
terminology -
node - member of array
tree - nodes in hierarchy
root - highest hierarchy in the tree
connected nodes - nodes with same root
basically append the smaller tree to the larger tree (can be size or height)

firstly we'd like to measure the tree size on the go (optional), then we just append
the shorter tree.

prof. didn't fully cover that but it can be proven that any tree is at a
maximal depth on log_2(N), that is due to the fact that another tree
is appended only if its at least as big as the other one
'''
import pandas as pd

from quick_union import QuickUnion
class WQU(QuickUnion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = [1 for _ in range(self.array_size)]

    def union(self, node_1_index , node_2_index):
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
    def generate_result_df(self):
        self.result = pd.DataFrame([self.id_array , self.size , self.array],index=['id' , 'size','values'  ])

