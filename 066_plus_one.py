from typing import List

class Solution:
    def plus_one(self, digits: int) -> List[int]:
        ls = len(digits)

        # reverse the index to increment from least significant value
        for i in reversed(range(ls)):

            # increment value in place and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # 9 becomes 0 and the next value will be incremented
            else:
                digits[i] = 0

        # you reached the most significate digit
        # insert another digit that starts from 1
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plus_one([9, 9, 9]))

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:
# Input: digits = [0]
# Output: [1]

# Example 4:
# Input: digits = [9, 9, 9]
# Output: [1, 0, 0, 0]