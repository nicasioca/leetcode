from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) 
        dp[0] = True
        
        # iterate over the word
        for i in range(1, len(s) + 1):

          # iterate over subsets of the word
          for j in range(i):

            # dp[j] up to this point is True and the other half exists in wordDict
            if dp[j] and s[j:i] in wordDict:
              dp[i] = True
              break

        return dp[-1]