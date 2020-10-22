class Solution:
    def unique_path(self, m: int, n: int) -> int:

        # create m x n matrix of zeros
        dmap = [[0] * n for _ in range(m)]

        # set 1s for the first column
        for i in range(m):
            dmap[i][0] = 1

        # set 1s for the first row
        for j in range(n):
            dmap[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                l = u = 0

                # look back by one row to get value
                if i-1 >= 0:
                    u = dmap[i-1][j]
                
                # look back by one column to get value
                if j-1 >= 0:
                    l = dmap[i][j-1]
                
                # aggregate the values to get the total unique paths at this point
                dmap[i][j] = l + u

        # return the final number of unique paths 
        # in the last row and column (the bottom-right corner)
        # based on with the proper zero based index values
        return dmap[m-1][n-1]


if __name__ == '__main__':
    # robot starts top-left and must end in bottom-right corner
    # robot can only move either down or right at any point in time
    s = Solution()
    print(s.unique_path(3, 7))
    # Output: 28