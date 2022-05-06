class Solution:
    def longestPalindrome(self, s):
        res = ''
        
        for i in range(len(s)):
            
            # odd case like "aba"
            tmp = self.helper(s, i, i)
            res = res if len(res) > len(tmp) else tmp
            
            # even case like "abba"
            tmp = self.helper(s, i, i+1)
            res = res if len(res) > len(tmp) else tmp
            
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
            
        # add back to left to be inclusive of the correct slice
        # right is already one further right so leave as is
        return s[l+1:r]


# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"