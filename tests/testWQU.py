from weighted_quick_union import WQU
'''
test1:
2 is fathering 0, 1
5 is fathering 3, 4
we merge 2,5 so that 5 fathers 0,1,2,3,4
9 fathers 7,8,6
we merge 9,5 so that 5 fathers everyone
'''
test1 = WQU(array_size=10)
test1.union(1 ,2)
test1.union(0 , 2)
test1.union(7 , 9)
test1.union(8 , 9)
test1.union(6 , 9)
test1.union(3 , 5)
test1.union(4 , 5)
test1.union(2, 5)
test1.union(9 , 5)
test1.generate_result_df()
# it works !
test2 = WQU(10000)
for node in range(len(test2.array)):
    test2.union(node, 0)


print('done')