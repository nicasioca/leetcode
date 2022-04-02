class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        row_size = len(matrix)
        col_size = len(matrix[0])
        for i in range(row_size):
            for j in range(col_size):
                # matrix[i][j] = 0
                if matrix[i][j] == 0:
                  rows.add(i)
                  cols.add(j)
        
        for i in range(row_size):
          for j in range(col_size):
            if i in rows or j in cols:
              matrix[i][j] = 0

# matrix1: [[1,1,1],[1,0,1],[1,1,1]]
# output1: [[1,0,1],[0,0,0],[1,0,1]]

# matrix2: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# output2: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]