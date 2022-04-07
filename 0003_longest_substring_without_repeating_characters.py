class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        mx = left = 0
        for right, c in enumerate(s):
            if c in seen:
                left = max(left, seen[c] + 1)
            seen[c] = right
            mx = max(mx, right-left+1)
        return mx

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcdefghijj'))
    # Output: 10
