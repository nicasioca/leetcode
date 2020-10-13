class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def merge_two_lists(self, l1, l2):

        # set beginning node
        pos = dummy_head = ListNode(-1)

        # sort list as you iterate over lists
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next

            # move current position to next position
            pos = pos.next

        # empty remaining node
        if l1 is not None:
            pos.next = l1
        if l2 is not None:
            pos.next = l2

        # return the head
        return dummy_head.next


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    one.next = two
    two.next = five

    three.next = four

    # 1 -> 2 -> 5
    l1 = one

    # 3 -> 4
    l2 = three

    # Input l1: 1 -> 2 -> 5
    print('\nInput l1:')
    while one is not None:
        if one.next != None:
            print(str(one.val) + ' -> ', end = '')
        else:
            print(str(one.val), end = '')
        one = one.next
    print('\n')

    # Input l2: 3 -> 4
    print('\nInput l2:')
    while three is not None:
        if three.next != None:
            print(str(three.val) + ' -> ', end = '')
        else:
            print(str(three.val), end = '')
        three = three.next
    print('\n')

    s = Solution()
    head_returned = s.merge_two_lists(l1, l2)

    # Output: 1 -> 2 -> 3 -> 4 -> 5
    print('\nOutput:')
    while head_returned is not None:
        if head_returned.next != None:
            print(str(head_returned.val) + ' -> ', end = '')
        else:
            print(str(head_returned.val), end = '')
        head_returned = head_returned.next
    print('\n')

