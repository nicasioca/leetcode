# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return 'x'

        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # self.data for global variable
        self.data = data
        if self.data[0] == 'x':
            return None
        
        node = TreeNode(self.data[:self.data.find(',')]) 
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])
        
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []