from quick_union import QuickUnion
import pandas as pd
'''
test 1:
index 0 is a child of 1
index 1 is parentless
index 2 is child of 1
index 3 is child of 1
index 4 is child of 3
index 5 is child of 4
'''
union_test_1 = QuickUnion(array= [1, 1, 1, 1, 3, 4] , array_size= 6)
union_test_1.get_root(node_index=0)

'''
test 2:
'''
union_test_2 = QuickUnion(array_size= 9)
'''
append 1 , 2 as children of 0
'''
union_test_2.union(0,1)
union_test_2.union(0,2)
'''
append 6 , 7 as children of 8
'''
union_test_2.union(6,8)
union_test_2.union(7,8)

result_2 = pd.DataFrame([union_test_2.id_array,union_test_2.array])
result_2.index = ['id' , 'value']
union_test_2.get_root(node_index=0)
print('done')

