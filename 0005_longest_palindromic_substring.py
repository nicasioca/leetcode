class Solution:
    def longest_palindrome(self, s: str) -> str:
        
        # Manacher algorithm
        #http://en.wikipedia.org/wiki/Longest_palindromic_substring
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking

        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):

            # As long as R is greater than i,
            # set the minimum for P
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        return s[ (center_index - max_len)//2 : (center_index + max_len)//2 ]


if __name__ == '__main__':
    s = Solution()
    print(s.longest_palindrome("banana"))
    