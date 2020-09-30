class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        
        # dummy head node to point to the beginning
        head = curr = ListNode(0)

        while l1 or l2:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            # hold single digit sum as next value
            curr.next = ListNode(val % 10)

            # point to the new next node
            curr = curr.next

            # carry 1 if 10 or over
            carry = int(val / 10)

        # carry over last carry value
        if carry > 0:
            curr.next = ListNode(carry)

        # return the linked list from the beginning
        return head.next

if __name__ == '__main__':
    # create linked list of 2 -> 4 -> 3
    one_three = ListNode(3)
    one_four = ListNode(4)
    one_two = ListNode(2)
    one_four.next = one_three
    one_two.next = one_four
    l1 = one_two

    # create linked list of 5 -> 6 -> 4
    two_four = ListNode(4)
    two_six = ListNode(6)
    two_five = ListNode(5)
    two_six.next = two_four
    two_five.next = two_six
    l2 = two_five

    s = Solution()

    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    answer = s.add_two_numbers(l1, l2)
    while answer:
        if answer.next != None:
            print(str(answer.val) + ' -> ', end = '')
        else:
            print(str(answer.val), end = '')
        answer = answer.next
    print()
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.