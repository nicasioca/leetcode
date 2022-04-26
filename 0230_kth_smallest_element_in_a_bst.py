# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


# # Recusive
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.k = k
#         self.res = None
#         self.helper(root)
#         return self.res

#     def helper(self, node):
#         if node == None:
#             return
#         self.helper(node.left)
#         self.k -= 1
#         if self.k == 0:
#             self.res = node.val
#             return
#         self.helper(node.right)
              

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
    
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
