"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m, visited = dict(), set()
        self.dfs(node, m, visited)
        return m[node]
        
    def dfs(self, n, m, visited):
        if n in visited:
            return 
        visited.add(n)
        if n not in m:
            m[n] = Node(n.val)
        for neigh in n.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
            self.dfs(neigh, m, visited)

    # # bfs
    # def cloneGraph1(self, node):
    #     if not node:
    #         return node
    #     m, visited, queue = {}, set(), collections.deque([node])
    #     while queue:
    #         n = queue.popleft()
    #         if n in visited:
    #             continue
    #         visited.add(n)
    #         if n not in m:
    #             m[n] = Node(n.val)
    #         for neigh in n.neighbors:
    #             if neigh not in m:
    #                 m[neigh] = Node(neigh.val)
    #             m[n].neighbors.append(m[neigh])
    #             queue.append(neigh)
    #     return m[node]
    
    # # dfs iteratively
    # def cloneGraph2(self, node):
    #     if not node:
    #         return node
    #     m, visited, stack = dict(), set(), deque([node])
    #     while stack:
    #         n = stack.pop()
    #         if n in visited:
    #             continue
    #         visited.add(n)
    #         if n not in m:
    #             m[n] = Node(n.val)
    #         for neigh in n.neighbors:
    #             if neigh not in m:
    #                 m[neigh] = Node(neigh.val)
    #             m[n].neighbors.append(m[neigh])
    #             stack.append(neigh)
    #     return m[node]


# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

