class LRUCache:

  def __init__(self, capacity: int):
      self.dic = collections.OrderedDict()
      self.remain = capacity

  def get(self, key: int) -> int:
      if key not in self.dic:
          return -1
      v = self.dic.pop(key) 
      self.dic[key] = v   # set key as the newest one
      return v

  def put(self, key: int, value: int) -> None:
      if key in self.dic:    
          self.dic.pop(key)
      else:
          if self.remain > 0:
              self.remain -= 1  
          else:  # self.dic is full
              self.dic.popitem(last=False) 
      self.dic[key] = value




# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4






# class ListNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.dic = dict() # key to node
#         self.capacity = capacity
#         self.head = ListNode(0, 0)
#         self.tail = ListNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         if key in self.dic:
#             node = self.dic[key]
#             self.removeFromList(node)
#             self.insertIntoHead(node)
#             return node.value
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:             # similar to get()        
#             node = self.dic[key]
#             self.removeFromList(node)
#             self.insertIntoHead(node)
#             node.value = value         # replace the value len(dic)
#         else: 
#             if len(self.dic) >= self.capacity:
#                 self.removeFromTail()
#             node = ListNode(key,value)
#             self.dic[key] = node
#             self.insertIntoHead(node)
			
#     def removeFromList(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
    
#     def insertIntoHead(self, node):
#         headNext = self.head.next 
#         self.head.next = node 
#         node.prev = self.head 
#         node.next = headNext 
#         headNext.prev = node
    
#     def removeFromTail(self):
#         if len(self.dic) == 0: return
#         tail_node = self.tail.prev
#         del self.dic[tail_node.key]
#         self.removeFromList(tail_node)
