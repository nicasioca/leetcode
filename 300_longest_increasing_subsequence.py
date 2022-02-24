class Solution:
    def lengthOfLIS(self, nums) -> int:
      n = len(nums)
      dp = [1] * n
      # print(dp)
      for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                # print(dp)

      # print(dp)
      return max(dp)

s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))

nums2 = [0,1,0,3,2,3]
print(s.lengthOfLIS(nums2))

nums3 = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(nums3))