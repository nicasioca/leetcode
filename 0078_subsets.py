from typing import Listv

class Solution:
    def subsets(self, nums: int) -> List[int]:
        nums.sort()
        res = [[]]
        for index in range(len(nums)):
            size = len(res)

            # use existing subsets to generate new subsets
            for j in range(size):

                # grab the current existing list
                curr = list(res[j])

                # append a number from the original list
                curr.append(nums[index])

                # add the new subset to the existing lists
                res.append(curr)

        return res

if __name__ == "__main__":
    s = Solution()

    # Note: The solution set must not contain duplicate subsets.
    print(s.subsets([1, 2, 3]))
    # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]