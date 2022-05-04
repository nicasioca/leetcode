from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        # check if the total number of characters are the same
        if sum(s_count.values()) != sum(t_count.values()):
            return False
            
        # check if the vals are the same and the val counts are the same
        for val in s_count:
            if not val in t_count or \
                s_count[val] != t_count[val]:
                return False
        
        return True


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false