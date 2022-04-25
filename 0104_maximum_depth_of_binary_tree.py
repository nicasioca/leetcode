# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthOfBinaryTree(node: Optional[TreeNode], count: int) -> int:
            if node == None:
                return count
            else:
                return max(maxDepthOfBinaryTree(node.left, count+1), maxDepthOfBinaryTree(node.right, count+1))
        return maxDepthOfBinaryTree(root, 0)


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2