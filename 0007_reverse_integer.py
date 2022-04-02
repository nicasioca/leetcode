class Solution:
    def reverse(self, x: int) -> int:
        
        res, is_pos = 0, 1

        # If negative, remember negative number
        # set the number to positive to handle
        if x < 0:
            is_pos = -1
            x = -1 * x

        # Using mod 10 leaves remainder
        # Floor division // removes remainder
        # res multiples by 10 to add number in reverse
        while x != 0:
            # Step 1) res: 3
            # Step 1) x: 12
            # Step 2) res: 32
            # Step 2) x: 1
            # Step 3) res: 321
            # Step 3) x: 0
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x //= 10

        return res * is_pos
        

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21