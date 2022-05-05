class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        word = []
        
        for char in s:
            if char in chars:
                word.append(char)
         
        l = 0
        r = len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True
            
  
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.