from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
      m_row = len(matrix)
      m_col = len(matrix[0])
      result = 0

      for row in range(1, m_row):
        for col in range(1, m_col):
          # print(m, n)
          if matrix[row-1][col-1] > 0 and \
             matrix[row-1][col] > 0 and \
             matrix[row][col-1] > 0 and \
             matrix[row][col] > 0:
            matrix[row][col] = min(matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1]) + 1
 
      for row in range(m_row):
        for col in range(m_col):
          result += matrix[row][col]
      return result

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(Solution().countSquares(matrix))
