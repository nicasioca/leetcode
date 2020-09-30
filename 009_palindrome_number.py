class Solution():
    def is_palindrome(self, x: int) -> bool:

        if x < 0:
            return False

        # reverse x
        rev_x = 0

        # temporarily hold the x value
        temp = x
        while temp != 0:
            curr = temp % 10 # take least significant value
            rev_x = rev_x * 10 + curr # add to reverse value the significant value
            temp = temp // 10 # cut the least significant value from x
            
        if rev_x == x:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(1001))
    
# STEP 0
# curr:  0
# rev_x:  0
# temp:  1001

# STEP 1
# curr:  1
# rev_x:  1
# temp:  100

# STEP 2
# curr:  0
# rev_x:  10
# temp:  10

# STEP 3
# curr:  0
# rev_x:  100
# temp:  1

# STEP 4
# curr:  1
# rev_x:  1001
# temp:  0

# FINAL OUTPUT
# True