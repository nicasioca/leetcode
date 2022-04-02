class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

      res = 0
      x = startValue
      y = target

      # modulus operation to calculate the minimum number of multiplications by 2
      while x < y:
          res += y % 2 + 1
          y = (y + 1) // 2

      # subtract y to get the number of subtract by 1 operations
      return res + x - y