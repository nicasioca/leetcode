class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        left = longest = 0
        used = {}
        for right, c in enumerate(s):
            if c in used and left <= used[c]:
                left = used[c] + 1
            else:
                longest = max(longest, right - left + 1)
            used[c] = right
        return longest

if __name__ == '__main__':
    s = Solution()
    print(s.length_of_longest_substring('abcdefghijj'))
    # Output: 10

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
