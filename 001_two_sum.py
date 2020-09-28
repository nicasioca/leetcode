class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # enumerate values to index 0 and index in index 1 of each tuple
        nums_index = [(v, index) for index, v in enumerate(nums)]

        # sort by the values in ascending order by index 0 of each tuple
        nums_index.sort()

        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]

            # match sum equals target return index 1 positions of the tuples
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            
            # sum too small increment from beginning to use larger number
            elif curr < target:
                begin += 1

            # sum too big decrement from end to use smaller number
            else:
                end -= 1

if __name__ == '__main__':
    s = Solution()
    # Input: nums = [3,2,4], target = 6
    print(s.two_sum([3, 2, 4], 6))
    # Output: [1,2]


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]