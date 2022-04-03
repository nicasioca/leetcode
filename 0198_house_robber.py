from typing import List

# same as house robber ii just without the houses in a circle
class Solution:
    def robHelper(self, nums: List[int], start: int, end: int) -> int:
        
        rob1, rob2 = 0, 0
        for i in range(start, end):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        
        house1 = self.robHelper(nums, 0, size)
        house2 = self.robHelper(nums, 1, size-1)
        
        return max(house1, house2)