# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q

# DFS with stack        
# def isSameTree2(self, p, q):
#     stack = [(p, q)]
#     while stack:
#         node1, node2 = stack.pop()
#         if not node1 and not node2:
#             continue
#         elif None in [node1, node2]:
#             return False
#         else:
#             if node1.val != node2.val:
#                 return False
#             stack.append((node1.right, node2.right))
#             stack.append((node1.left, node2.left))
#     return True
 
# BFS with queue    
# def isSameTree3(self, p, q):
#     queue = [(p, q)]
#     while queue:
#         node1, node2 = queue.pop(0)
#         if not node1 and not node2:
#             continue
#         elif None in [node1, node2]:
#             return False
#         else:
#             if node1.val != node2.val:
#                 return False
#             queue.append((node1.left, node2.left))
#             queue.append((node1.right, node2.right))
#     return True


# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
