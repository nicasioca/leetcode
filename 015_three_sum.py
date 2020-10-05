class Solution:
    def three_sum(self, nums: [int], target: int) -> [[int]]:

        results = []

        # sort values
        nums.sort()

        last = len(nums)
        for i in range(last - 2):

            # move i until matching
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = last - 1


            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                # match curr equals target add solution to array of answers
                if curr == target:
                    results.append([nums[i], nums[j], nums[k]])

                    # move j and k until matching
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

                # curr too small increment from beginning to use larger number
                elif curr < target:
                    j += 1

                # curr too big decrement from end to use smaller number
                else:
                    k -= 1
        return results

if __name__ == '__main__':
    s = Solution()
    # Input: nums = [-2, 5, 0, -1, 4, -3, 0], target = 0
    print(s.three_sum([-2, 5, 0, -1, 4, -3, 0], 0))
    # Output: [[-3, -2, 5], [-3, -1, 4]]