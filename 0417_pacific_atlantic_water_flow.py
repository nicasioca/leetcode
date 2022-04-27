class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not heights:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)




# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]




# This is a DFS Template to solve matrix questions:

# def dfs(matrix):
#     # 1. Check for an empty graph.
#     if not matrix:
#         return []

#     # 2. Initialize
#     rows, cols = len(matrix), len(matrix[0])
#     visited = set()
#     directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

#     def traverse(i, j):
#         # a. Check if visited
#         if (i, j) in visited:
#             return
# 		# b. Else add to visted
#         visited.add((i, j))

#         # c. Traverse neighbors.
#         for direction in directions:
#             next_i, next_j = i + direction[0], j + direction[1]
#             if 0 <= next_i < rows and 0 <= next_j < cols:
#                 # d. Add in your question-specific checks.
#                 traverse(next_i, next_j)

#     # 3. For each point, traverse it.
#     for i in range(rows):
#         for j in range(cols):
#             traverse(i, j)
