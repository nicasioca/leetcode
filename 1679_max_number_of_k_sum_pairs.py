class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_of_pairs_removed = 0
        dict_of_lists = defaultdict(list)
        
        for i, val in enumerate(nums):
            dict_of_lists[val].append(i)
        
        for val in nums:
            diff_val = k - val
            
            if val == diff_val:
                if len(dict_of_lists[val]) > 1:
                    dict_of_lists[val].pop(0)
                    dict_of_lists[val].pop(0)
                    num_of_pairs_removed += 1
            else:
                if len(dict_of_lists[val]) > 0 and len(dict_of_lists[diff_val]) > 0:
                    dict_of_lists[val].pop(0)
                    dict_of_lists[diff_val].pop(0)
                    num_of_pairs_removed += 1
                    
        return num_of_pairs_removed
                

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

