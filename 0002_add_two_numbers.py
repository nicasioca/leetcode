# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0

    # dummy head node to point to the beginning
    head = curr = ListNode(0)

    while l1 or l2:
      # add carry value to current column
      val = carry

      # grab column values and add them together
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
  l1 = ListNode(2, ListNode(4, ListNode(3)))

  # create linked list of 5 -> 6 -> 4
  l2 = ListNode(5, ListNode(6, ListNode(4)))

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
