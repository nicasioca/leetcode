from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        head = dummy = ListNode(0)
        
        for index, l in enumerate(lists):
            if l:
                heappush(h, (l.val, index))
            print('before', h)

        while h:
            val, min_index = heappop(h)

            tmp = ListNode(val)
            while dummy.next:
                dummy = dummy.next
            dummy.next = tmp
            
            if lists[min_index].next:
                lists[min_index] = lists[min_index].next
                heappush(h, (lists[min_index].val, min_index))
            print('after', h)
            
        return head.next

lists = [ListNode(1, ListNode(4, ListNode(5))), 
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]

linked_list = Solution().mergeKLists(lists)
while linked_list:
  print(linked_list.val)
  linked_list = linked_list.next