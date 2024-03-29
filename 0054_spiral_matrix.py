class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        
        # current values (i,j) and dynamic increment values (di, dj)
        i = 0
        j = 0
        di = 0
        dj = 1
        
        # iterate over the entire size of the final list size (m * n)
        for _ in range(size):
            
            # go ahead and add to the list
            result.append(matrix[i][j])
            matrix[i][j] = '.'
            
            # 0,0 0,1 0,2     -> 1,2 2,2        -> 2,1 2,0         -> 1,0           -> 1,1
            # go right (0, 1) -> go down (1, 0) -> go left (0, -1) -> go up (-1, 0) -> go right (0, 1)
            
            # look ahead to see if out-of-bounds or already processed
            if (i + di) < 0 or (j + dj) < 0 or (i + di) >= m or (j + dj) >= n or matrix[(i + di)][(j + dj)] == '.':
                di, dj = dj, -di
            
            # increment each step
            i += di
            j += dj
            
        return result
                
                    
                    

# from typing import List

# class Solution:
#     def spiral_order(self, matrix: List[List[int]]) -> List[int]:
#         result = []

#         if not matrix:
#             return []

#         # set the indices
#         # for the variables to rotate
#         i, j, di, dj = 0, 0, 0, 1

#         # get rows by columns size
#         m, n = len(matrix), len(matrix[0])

#         for v in range(m * n):

#             # append the current position i, j
#             result.append(matrix[i][j])

#             # set to empty after you've copied the current position
#             matrix[i][j] = ''

#             # modulus row and column to see if empty before shifting spiral position
#             if matrix[(i + di) % m][(j + dj) % n] == '':
#                 # down (1, 0) -> left (0, -1) -> up (-1, 0) -> right (0, 1)
#                 di, dj = dj, -di

#             # add i, j to latest di, dj values to keep iterating or shift value position
#             i += di
#             j += dj

#         return result


if __name__ == '__main__':
    s = Solution()
    # print(s.spiral_order([[ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ]]))
    # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    print(s.spiral_order([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]))
    # i, j, di, dj = 0, 0, 0, 1

    # Append: [0][0] =  1
    # Iterate: (i + di, j + dj) = ( 0 ,  1 )

    # Append: [0][1] =  2
    # Iterate: (i + di, j + dj) = ( 0 ,  2 )

    # Append: [0][2] =  3
    # Shift: ( (i + di) % m , (j + dj) % n ) == ( 0 ,  0 ) == ''
    # before di, dj =  0 1
    # after di, dj = dj, -di
    # after di, dj =  1 0
    # Iterate: (i + di, j + dj) = ( 1 ,  2 )

    # Append: [1][2] =  6
    # Iterate: (i + di, j + dj) = ( 2 ,  2 )

    # Append: [2][2] =  9
    # Shift: ( (i + di) % m , (j + dj) % n ) == ( 0 ,  2 ) == ''
    # before di, dj =  1 0
    # after di, dj = dj, -di
    # after di, dj =  0 -1
    # Iterate: (i + di, j + dj) = ( 2 ,  1 )

    # Append: [2][1] =  8
    # Iterate: (i + di, j + dj) = ( 2 ,  0 )

    # Append: [2][0] =  7
    # Shift: ( (i + di) % m , (j + dj) % n ) == ( 2 ,  2 ) == ''
    # before di, dj =  0 -1
    # after di, dj = dj, -di
    # after di, dj =  -1 0
    # Iterate: (i + di, j + dj) = ( 1 ,  0 )

    # Append: [1][0] =  4
    # Shift: ( (i + di) % m , (j + dj) % n ) == ( 0 ,  0 ) == ''
    # before di, dj =  -1 0
    # after di, dj = dj, -di
    # after di, dj =  0 1
    # Iterate: (i + di, j + dj) = ( 1 ,  1 )

    # Append: [1][1] =  5
    # Shift: ( (i + di) % m , (j + dj) % n ) == ( 1 ,  2 ) == ''
    # before di, dj =  0 1
    # after di, dj = dj, -di
    # after di, dj =  1 0
    # Iterate: (i + di, j + dj) = ( 2 ,  1 )

    # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]