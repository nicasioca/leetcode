class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlen = 0

        # take a number and count the consecutive first to last numbers
        while nums:
            first = last = nums.pop()
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            while last + 1 in nums:
                last += 1
                nums.remove(last)

            # calculate the largest consecutive numbers between first and last
            maxlen = max(maxlen, last - first + 1)
            
        return maxlen


# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9