from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_dict = defaultdict(set)
        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.Visited = [0] * numCourses
        self.Ans, self.FoundCycle = [], 0
        
        for i in range(numCourses):
            if self.FoundCycle == 1: break      # early stop if the loop is found
            if self.Visited[i] == 0:
                self.dfs(i)
     
        return [] if self.FoundCycle == 1 else self.Ans

    def dfs(self, start: int):
        if self.FoundCycle == 1:   return     # early stop if the loop is found    
        if self.Visited[start] == 1:
            self.FoundCycle = 1               # loop is found
        if self.Visited[start] == 0:           # node is not visited yet, visit it
            self.Visited[start] = 1             # color current node as gray
            for neighb in self.adj_dict[start]:   # visit all its neighbour
                self.dfs(neighb)
            self.Visited[start] = 2             # color current node as black
            self.Ans.append(start)              # add node to answer




# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
