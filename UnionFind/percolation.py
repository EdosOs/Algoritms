'''
percolation - imagine n x n matrix where each cell is either black or white.
we want to know whether we can arrive from the upper to the lower row of
the matrix where travel is allowed only through white cells.
terminology:
white connected cells area is called open site
black connected cells area is called closed site
we define a matrix as 'percolates' if there is an open site that connects
top to bottom.

we define the probability of a cell to be white as p
model:

percolation phase transition - if p > 0.593


solving percolation using union find:
we give each cell in the matrix id and union the cells that are connected
through white spaces.

if any cell on the bottom row has the same root as the cell at the top row
the matrix is percolated.
'''
from weighted_quick_union_path_comp import WQUPC
class percolation(WQUPC):
    pass