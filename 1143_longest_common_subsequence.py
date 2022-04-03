class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [ [0] * (n+1) for _ in range(m+1) ]

        for i in range(m):
            for j in range(n):

                # if character exists in both add 1 to current at next position
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1

                # else character doesn't exist, carry forward the previous max match
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        # return the bottom right value for the longest common subsequence
        return dp[-1][-1]


text1 = "ace"
text2 = "abcde" 
# Output: 3
# text1 = "abc"
# text2 = "def"
# Output: 0
print(Solution().longestCommonSubsequence(text1, text2))