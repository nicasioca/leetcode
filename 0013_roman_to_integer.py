class Solution:
    def roman_to_int(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        curr, prev = 0, 0
        total = 0
        for c in s:
            curr = roman[c]
            total += curr # add the current value

            # if I, X, or C came before a larger current value
            if curr > prev:
                # subtract what you added before and subtract again for being a lower value
                total -= (prev + prev)

            prev = curr # set previous value from current value

        return total

if __name__ == '__main__':
    s = Solution()
    print(s.roman_to_int('MCMXCIV'))

# STEP 0
# c: M
# curr: 1000
# prev: 0
# total: 1000

# STEP 1
# c: C
# curr: 100
# prev: 1000
# total: 1100

# STEP 2
# c: M
# curr: 1000
# prev: 100
# total: 1900

# STEP 3
# c: X
# curr: 10
# prev: 1000
# total: 1910

# STEP 4
# c: C
# curr: 100
# prev: 10
# total: 1990

# STEP 5
# c: I
# curr: 1
# prev: 100
# total: 1991

# STEP 6
# c: V
# curr: 5
# prev: 1
# total: 1994

# FINAL STEP
# 1994
