class Solution:
    def unique_paths_with_obstacles(self, obstacle_grid: [[int]]) -> int:

        # get size of matrix by rows and columns
        m, n = len(obstacle_grid), len(obstacle_grid[0])

        # return 0 if no paths
        if m == 0:
            return 0

        # create zero (m + 1) x (n + 1) matrix of zeros
        dmap = [[0] * (n + 1) for _ in range(m + 1)]

        # set the initial value of the (m - 1) x (n + 1) matrix bottom right as one
        dmap[m - 1][n] = 1

        # now work backwards decrementing by row and column until you hit negative one
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # set obstacle as zero value
                if obstacle_grid[i][j] == 1:
                    dmap[0][0] = 0

                # otherwise, add to the number of paths
                else:
                    dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]

        # final number of paths is in top left
        return dmap[0][0]

if __name__ == "__main__":
    s = Solution()
    obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.unique_paths_with_obstacles(obstacle_grid))
    # Output: 2