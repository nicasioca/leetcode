from collections import Counter
from heapq import heapify,heappush, heappop

class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = Counter(S)
        heap = [(-v,k) for k,v in cnt.items()]
        heapify(heap)
        ans = []
        while(len(heap)>1):
            x = heappop(heap)
            y = heappop(heap)
            ans.extend([x[1],y[1]])
            if x[0]<-1:
                heappush(heap,(x[0]+1,x[1]))
            if y[0]<-1:
                heappush(heap,(y[0]+1,y[1]))
        if heap:
            if heap[0][0]<-1:
                return "" # case where last left element count is more than 2
            ans.append(heap[0][1])
        return "".join(ans)




# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""
