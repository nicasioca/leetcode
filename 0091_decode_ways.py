class Solution:
    def numDecodings(self, s: str) -> int:

        # set the characters from 1 to 26 (for A to Z)
        char = {str(x) for x in range(1, 27)}
        
        # handle base case of size 1
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        
        # setup array to track number of combinations
        dp = [0] * (len(s)+1)
        
        # Verify valid characters and set base case values
        if s[0] in char:
            dp[0], dp[1] = 1, 1
        else:
            return 0
        
        # verify characters and handle double digit values and single digit values
        # add to the value as you iterate forward in the array
        for i in range(1, len(s)):
            if s[i-1:i+1] in char:
                if s[i] == '0':
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = dp[i-1] + dp[i]
            else:
                if s[i] == '0':
                    return 0
                else:
                    dp[i+1] = dp[i]
                  
        # return the last value to get the total combinations
        return dp[-1]


# s = "12"
# Output: 2
s = "226"
# Output: 3
# s = "06"
# Output: 0
print(Solution().numDecodings(s))