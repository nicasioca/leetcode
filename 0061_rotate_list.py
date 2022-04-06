# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        zero = ListNode(next=head) # dummy node
        
        count, tail = 0, zero
        while tail.next:
            count, tail = count + 1, tail.next
            
        k = k % count
        if not k: return head

        newTail = zero
        for _ in range(0, count - k):
            newTail = newTail.next

        zero.next, tail.next, newTail.next = newTail.next, head, None
            
        return zero.next


# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
