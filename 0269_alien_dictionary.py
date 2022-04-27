from typing import List
from heapq import *

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Construct Graph
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos+1]))):
                pre, next = words[pos][i], words[pos+1][i]
                if pre != next:
                    in_degree[next] += 1
                    neighbors[pre].append(next)
                    break
        
        # Topological Sort
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            for _ in range(len(heap)):
                ch = heappop(heap)
                order.append(ch)
                for child in neighbors[ch]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        heappush(heap, child)
        
        # order is invalid
        if len(order) != len(in_degree):
          return ""
        return ''.join(order)


# class Solution:
#     """
#     @param words: a list of words
#     @return: a string which is correct order
#     """

#     def alienOrder(self, words):
#         # Write your code here
#         from collections import defaultdict
#         from collections import deque
#         import heapq
        
#         graph = {}

#         # initial graph
#         for w in words:
#             for c in w:
#                 graph[c] = set()
        
#         for i in range(1, len(words)):
#             for j in range(min(len(words[i]), len(words[i-1]))):
#                 if words[i-1][j] != words[i][j]:
#                     graph[words[i-1][j]].add(words[i][j])
#                     break

#         indegree = defaultdict(int)
#         for g in graph:
#             for ne in graph[g]:
#                 indegree[ne] += 1

#         q = [w for w in graph if indegree[w] == 0]
#         heapq.heapify(q)

#         order = []
#         visited = set()
#         while q:
#             # n = q.pop()
#             n = heapq.heappop(q)

#             if n in visited:
#                 continue
#             visited.add(n)
#             order.append(n)

#             for ne in graph[n]:
#                 indegree[ne] -= 1
#                 if indegree[ne] == 0:
#                     # q.appendleft(ne)
#                     heapq.heappush(q, ne)
#         return ''.join(order) if len(order) == len(graph) else ''


# Example 1:
# Input：["wrt","wrf","er","ett","rftt"]
# Output："wertf"
# Explanation：
# from "wrt"and"wrf" ,we can get 't'<'f'
# from "wrt"and"er" ,we can get 'w'<'e'
# from "er"and"ett" ,we can get 'r'<'t'
# from "ett"and"rftt" ,we can get 'e'<'r'
# So return "wertf"

# Example 2:
# Input：["z","x"]
# Output："zx"
# Explanation：
# from "z" and "x"，we can get 'z' < 'x'
# So return "zx"