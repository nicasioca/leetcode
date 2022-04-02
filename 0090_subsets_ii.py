class Solution:
    def subsets_with_dups(self, nums: int) -> int:
        nums.sort()
        res = [[]]

        # Step 1: add variable to handle duplicates
        begin = 0

        for index in range(len(nums)):

            # Step 2: account for all by checking if different
            if index == 0 or nums[index] != nums[index - 1]:
                begin = 0

            size = len(res)

            # use existing subsets to generate new subsets
            for j in range(begin, size):

                # grab the current existing list
                curr = list(res[j])

                # append a number from the original list
                curr.append(nums[index])

                # add the new subset to the existing lists
                res.append(curr)

            # Step 3: set the new beginning size to avoid duplicate subsets
            begin = size

        return res

if __name__ == "__main__":
    s = Solution()

    # Note: The solution set must not contain duplicate subsets.
    print(s.subsets_with_dups([1, 2, 2]))
    # Output: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]