from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if max_reach < i:  # max_reach cannot reach position i
                return False
            max_reach = max(max_reach, i + n)
        return True




# nums = [2,3,1,1,4]
# Output: True
# nums = [3,2,1,0,4] 
# Output: False
nums = [1]
# Output: True
print(Solution().canJump(nums))