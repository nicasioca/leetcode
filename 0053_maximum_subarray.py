class Solution:
    def max_sub_array(self, nums: list) -> list:

        # set the max ending here and max so far to the first value
        max_ending_here = max_sub_so_far = nums[0]

        # for the rest of the list find the max at each point
        for i in range(1, len(nums)):

            # find the max at this point, which is the aggregate value or current value
            max_ending_here = max(max_ending_here + nums[i], nums[i])

            # compare the max here to the the max so far to get latest max so far
            max_sub_so_far = max(max_ending_here, max_sub_so_far)

        # return the latest max so far
        return max_sub_so_far


if __name__ == '__main__':
    s = Solution()
    print(s.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.
