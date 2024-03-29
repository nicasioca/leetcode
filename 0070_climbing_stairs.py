class Solution:
    def climbing_stairs(self, n: int) -> int:

      # start with 1 step or 2 steps
      step1, step2 = 1, 1

      # otherwise, calculate the additional ways
      for i in range(n):
        temp = step2
        step2 = step1 + step2
        step1 = temp
      
      # return the total numbers of ways to step from step1
      return step1


if __name__ == '__main__':
    s = Solution()
    print(s.climbing_stairs(6))
    # Output: 13

# Example 1
# Input: 2
# Output: 2

# Explanation: 1 distinct path of all 1s
# 1. 1 step + 1 step

# Explanation: 1 distinct path of all 2s
# 2. 2 steps


# Example 2
# Input: 3
# Output: 3

# Explanation: 1 distinct path of all 1s
# 1. 1 step + 1 step + 1 step

# Explanation: 2 distinct combintations of paths
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Example 3
# Input: 4
# Output: 5

# Explanation: 2 distinct paths of all 1s and all 2s
# 1. 1 step + 1 step + 1 step + 1 step <-- all ones
# 2. 2 steps + 2 steps <-- all twos

# Explanation: 3 distinct combinations of paths, 
# the prevoius number of distinct paths
# 3. 1 step + 1 step + 2 steps
# 4. 1 step + 2 steps + 1 step
# 5. 2 steps + 1 step + 1 step


# Example 4
# Input: 5
# Output: 8

# Explanation: 3 distinct paths previously
# 1. 1 step + 1 step + 1 step + 1 step + 1 step <-- all ones
# 2. 2 steps + 2 steps + 1 step
# 3. 2 steps + 1 step + 2 steps 

# Explanation: 5 distinct paths previously
# 4. 1 step + 2 step + 2 steps
# 5. 2 step + 1 step + 1 step + 1 step
# 6. 1 step + 2 steps + 1 step + 1 step
# 7. 1 step + 1 step + 2 steps + 1 step
# 8. 1 step + 1 step + 1 step + 2 steps

# NOTE: at this point you realize 
# this is the Fibonacci Sequence 
# Xn = Xn-1 + Xn-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…