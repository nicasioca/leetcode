class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      graph = [[] for _ in range(numCourses)]
      visit = [0 for _ in range(numCourses)]

      for x, y in prerequisites:
          graph[x].append(y)

      def dfs(i):
          if visit[i] == -1:
              return False

          if visit[i] == 1:
              return True

          visit[i] = -1
          for j in graph[i]:
              if not dfs(j):
                  return False
          visit[i] = 1

          return True

      for i in range(numCourses):
          if not dfs(i):
              return False

      return True
# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.




# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
