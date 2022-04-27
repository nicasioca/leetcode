# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root == None or root == p or root == q:
                return root

            # Find p/q in left subtree
            l = self.lowestCommonAncestor(root.left, p, q)

            # Find p/q in right subtree
            r = self.lowestCommonAncestor(root.right, p, q)

            # If p and q found in left and right subtree of this node, then this node is LCA
            if l and r:
                return root

            # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
            return l if l else r
        
        
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
    
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1