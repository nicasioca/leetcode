class Solution:
    def characterReplacement(self, s: str, k: int) -> int:   
        
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1
            
            window_len = r - l + 1
            if window_len - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, window_len)
            else:
                c_frequency[s[l]] -= 1
                l += 1    
                
        return longest_str_len


# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
