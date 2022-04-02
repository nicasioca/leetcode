class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        
        # return None if head is None
        if head is None:
            return None

        # set slow and fast equal to head
        slow = fast = head

        # create a difference of n nodes
        for i in range(n):
            fast = fast.next

        # if you go n and equal to None
        # then head next should be returned
        if fast is None:
            head = head.next
            return head

        # while fast.next is not None
        # increment slow.next too
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # skip to next slow value
        # in order to remove nth node from end
        curr = slow.next
        slow.next = curr.next
        return head
        
if __name__ == '__main__':
    five = ListNode(5)

    four = ListNode(4)
    four.next = five

    three = ListNode(3)
    three.next = four

    two = ListNode(2)
    two.next = three

    one = ListNode(1)
    one.next = two

    n = 2
    head = one

    # Given a linked list, remove the n-th node from the end of list and return its head.

    # Example:
    # Given linked list: 1->2->3->4->5, and n = 2.
    # Given n will always be valid.
    print('\nInput:')
    while one is not None:
        if one.next != None:
            print(str(one.val) + ' -> ', end = '')
        else:
            print(str(one.val), end = '')
        one = one.next

    s = Solution()
    head_returned = s.remove_nth_from_end(head, n)

    # After removing the second node from the end, the linked list becomes 1->2->3->5.
    print('\n\nOutput:')
    while head_returned is not None:
        if head_returned.next != None:
            print(str(head_returned.val) + ' -> ', end = '')
        else:
            print(str(head_returned.val), end = '')
        head_returned = head_returned.next
    print('\n')

