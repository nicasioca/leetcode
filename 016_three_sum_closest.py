class Solution():
    def three_sum_closest(self, nums: [int], target: int) -> int:
        ls = len(nums)
        sort_nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(ls - 2):
            j, k = i + 1, ls - 1
            while j < k:
                temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
                if abs(target - temp) < abs(target - res):
                    res = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.three_sum_closest([-1, 2, 1, -4], 1))
    # Input: nums = [-1, 2, 1, -4], target = 1
    # Output: 2
    # Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).