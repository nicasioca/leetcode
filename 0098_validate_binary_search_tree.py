import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_valid_bst(self, root):
        return self.is_valid_helper(root, -sys.maxsize - 1, sys.maxsize)

    def is_valid_helper(self, root: TreeNode, min_val: int, max_val: int) -> bool:
        if root is None:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.is_valid_helper(root.left, min_val, root.val) and self.is_valid_helper(root.right, root.val, max_val)


if __name__ == '__main__':
    five = TreeNode(5)
    one = TreeNode(1)
    four = TreeNode(4)
    three = TreeNode(3)
    six = TreeNode(6)

    five.left = one
    five.right = four
    four.left = three
    four.right = six

    s = Solution()
    print(s.is_valid_bst(five))
    # Output: False

    # two = TreeNode(2)
    # two.left = one
    # two.right = three
    # print(s.is_valid_bst(two))
    # Output True


    # Example 1:

    #     2
    #    / \
    #   1   3

    # Input: [2,1,3]
    # Output: true
    # Example 2:

    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6

    # Input: [5,1,4,null,null,3,6]
    # Output: false
    # Explanation: The root node's value is 5 but its right child's value is 4.
    