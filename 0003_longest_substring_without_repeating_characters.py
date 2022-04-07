class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start) # update the res
                start = max(start, dic[ch]+1)  # here should be careful, like "abba"
            dic[ch] = i
        return max(res, len(s)-start)  # return should consider the last non-repeated substring

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcdefghijj'))
    # Output: 10
