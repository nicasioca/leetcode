# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    current_max = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, root):
        if root == None:
            return root
        
        left = self.maxPathSumHelper(root.left)
        if left == None or left < 0:
            left = 0
            
        right = self.maxPathSumHelper(root.right)
        if right == None or right < 0:
            right = 0
                
        self.current_max = max(left+right+root.val, self.current_max)

        # take the next node on the path with the maximum value
        return max(left, right) + root.val


# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
