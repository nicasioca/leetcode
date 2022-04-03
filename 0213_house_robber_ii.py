from typing import List

class Solution:
  def robHelper(self, nums, start, end):

        # iterate through each house for max value
        rob1, rob2 = 0, 0
        for n in range(start, end):
            temp = max(nums[n] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    
  def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # rob the 1st house
        money1 = self.robHelper(nums, 0, len(nums)-1)

        # rob the 2nd house
        money2 = self.robHelper(nums, 1, len(nums))

        return max(money1, money2)


# nums = [2,3,2]
# Output: 3
# nums = [1,2,3,1]
# Output: 4
nums = [4,1,2,7,5,3,1]
# Output: 14
print(Solution().rob(nums))