class Solution:
    def my_atoi(self, s: str) -> int:
        
        try:
            s = s.lstrip() + '$' # remove leading spaces and append an end mark

            # iterator through string until it hits a none valid character
            # return a valid result or show the value is too big for an integer
            for i, ch in enumerate(s):
                if not (ch in '+-' or '0' <= ch <= '9'):
                    result = int(s[:i])
                    return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
        
        except:
            # return 0 for all invalid results
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.my_atoi("4193 with words"))


# Example 1:
# Input: "42"
# Output: 42

# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
# Thefore INT_MIN (−231) is returned.