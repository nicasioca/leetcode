import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # stack solution
    # def in_order_traversal(self, root: TreeNode) -> [int]:
    #     res = []
    #     stack = []
    #     while root is not None:

    #         # retain the parent nodes as you go left
    #         stack.append(root)

    #         # keep going left until you hit furthest left node
    #         root = root.left

    #         # if root is None start tracking order
    #         while root is None:
    #             if len(stack) == 0:
    #                 return res

    #             # track left first
    #             root = stack.pop()
    #             res.append(root.val)

    #             # then go right to track
    #             root = root.right

    #     return res

    # recursive solution
    def in_order_traversal(self, root: TreeNode) -> [int]:
        res = []
        self.in_order_traversal_helper(res, root)
        return res

    def in_order_traversal_helper(self, res: [int], curr: TreeNode):
        # base case return None
        if curr is None:
            return

        # go left and keep going left until None
        if curr.left is not None:
            self.in_order_traversal_helper(res, curr.left)

        # start tracking the nodes
        res.append(curr.val)

        # go right to track anything right of that node
        if curr.right is not None:
            self.in_order_traversal_helper(res, curr.right)


if __name__ == '__main__':
    four = TreeNode(4)
    one = TreeNode(1)
    five = TreeNode(5)
    three = TreeNode(3)
    six = TreeNode(6)

    four.left = one
    four.right = five
    five.left = three
    five.right = six

    s = Solution()
    print(s.in_order_traversal(four))
    # Output: [1, 4, 3, 5, 6]

    two = TreeNode(2)
    two.left = one
    two.right = three
    # print(s.in_order_traversal(two))
    # Output: [1, 2, 3]


    # In order traversal
    # Example 1:
    #     2
    #    / \
    #   1   3
    # Input: [2, 1, 3]
    # Output: [1, 2, 3]

    # Example 2:
    #     4
    #    / \
    #   1   5
    #      / \
    #     3   6
    # Input: [4, 1, 5, null, null, 3, 6]
    # Output: [1, 4, 3, 5, 6]