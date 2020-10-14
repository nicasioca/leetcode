class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def swap_pairs(self, head: ListNode) -> ListNode:
        
        # create dummy to point to head
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # a is the previous node
        # b is the current node
        a, b = dummy_head, head
        while b != None and b.next != None:
            
            # get the next two nodes
            c = b.next
            d = b.next.next

            # re-wire the adjacent node pointers
            a.next = c
            c.next = b
            b.next = d

            # a becomes b the previous node
            # b becomes d which is the current node
            a = b
            b = d

        return dummy_head.next

if __name__ == '__main__':
    s = Solution()

    six = ListNode(6)

    five = ListNode(5)
    five.next = six
    
    four = ListNode(4)
    four.next = five
    
    three = ListNode(3)
    three.next = four

    two = ListNode(2)
    two.next = three

    one = ListNode(1)
    one.next = two

    head = one

    # Given a linked list, swap the adjacent nodes

    # Example:
    # Given linked list: 1->2->3->4->5->6
    print('\nInput:')
    while one is not None:
        if one.next != None:
            print(str(one.val) + ' -> ', end = '')
        else:
            print(str(one.val), end = '')
        one = one.next

    s = Solution()
    head_returned = s.swap_pairs(head)

    # The linked list becomes 2->1->4->3->6->5
    print('\n\nOutput:')
    while head_returned is not None:
        if head_returned.next != None:
            print(str(head_returned.val) + ' -> ', end = '')
        else:
            print(str(head_returned.val), end = '')
        head_returned = head_returned.next
    print('\n')

