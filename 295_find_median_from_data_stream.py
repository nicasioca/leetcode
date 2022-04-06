class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return 
        l = 0
        r = len(self.nums)-1
        while l < r:
            m = (l+r)//2
            if self.nums[m] == num:
                self.nums.insert(m,num)
                return 
            elif self.nums[m] < num:
                l = m+1
            else:
                r = m-1      
        if self.nums[l] < num:
            self.nums.insert(l+1,num)
        else:
            self.nums.insert(l,num)

    def findMedian(self) -> float:
        mid = (0 + len(self.nums)-1 )//2
        if (len(self.nums)-1) & 1:
            return (self.nums[mid] + self.nums[mid+1])/2
        else:
            return self.nums[mid]




# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
