class Solution:
    def edit_distance(self, word1: str, word2: str) -> int:
        ls_1, ls_2 = len(word1), len(word2)

        # create a placeholder to track number of inserts, deletes, and replacements
        dp = list(range(ls_1 + 1))

        # iterate the length of word2 + 1
        for j in range(1, ls_2 + 1): 

            # hold the first index position as the previous value
            pre = dp[0]

            # iterate the length of word1 + 1
            for i in range(1, ls_1 + 1):

                # hold original current index value
                temp = dp[i]

                # if matched, assign the previous placeholder value to note no change
                if word1[i - 1] == word2[j - 1]:
                    dp[i] = pre

                # increment the lowest of the previous, current, or next value of changes
                else:
                    dp[i] = min(pre + 1, dp[i - 1] + 1, dp[i] + 1)

                # set previous value to the current temp value
                pre = temp

        # final value is the number of changes to match word1
        return dp[ls_1]


if __name__ == '__main__':
    s = Solution()
    # print(s.edit_distance('horse', 'ros'))
    # Output: 3

    print(s.edit_distance('intention', 'execution'))
    # Output: 5