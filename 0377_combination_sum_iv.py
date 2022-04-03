from typing import List

class Solution(object):
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break # too big to accept
                if num == i: combs[i] += 1 # add divisible number
                if num  < i: combs[i] += combs[i - num] # add previous comb counts
        
        return combs[target]

nums = [1,2,3]
target = 4
print(Solution().combinationSum4(nums, target))