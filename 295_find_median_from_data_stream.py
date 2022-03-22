# 20/21 by basic logic but times out on the 21st case
# class MedianFinder:

#     def __init__(self):
#         self.input = []

#     def addNum(self, num: int) -> None:
#         self.input.append(num)
#         self.input.sort()

#     def findMedian(self) -> float:
#         size = len(self.input)
#         if size % 2 == 1:
#             index = int((size + 1) / 2 - 1)
#             return self.input[index]
#         else:
#             l_index = int(size / 2 - 1)
#             r_index = l_index + 1
#             return (self.input[l_index] + self.input[r_index]) / 2


# 21/21 cases passed without timing out
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap to store smaller half
        self.large = []   # min heap to store larger half

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)
        
        while len(self.small) - len(self.large) > 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        
        while len(self.large) - len(self.small) > 1:
            val = -heappop(self.large)
            heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0]+self.large[0])/2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        return self.large[0]