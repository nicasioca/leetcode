class Solution():
    def search_insert(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l + r) / 2)

            # look right (set l to floor) 
            # if num is less than target
            if nums[mid] < target:
                l = mid + 1

            # look left (set r to ceiling) 
            # if num is greater than target
            else:
                r = mid

        # target not found, nums is not the target
        # increment position to where it would be
        if nums[l] < target:
            return l + 1

        return l

if __name__ == '__main__':
    s = Solution()
    print(s.search_insert([1, 3, 5, 6], 5))
    # Output: 2