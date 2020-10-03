class Solution:
    def max_area(self, height: [int]) -> int:
        # Two points/walls to figure the max amount of water
        left, right = 0, len(height) - 1
        result = 0

        while left < right:

            # Calculate the minimum hight and multiply by the difference for latest area
            # If the latest max area is less than the previous result keep previous area
            result = max( min(height[left], height[right]) * (right - left), result)
            if height[left] > height[right]:
              # remove right to see if there is a higher right side to hold more water
              right -= 1
            else:
              # remove left to see if there is a higher left side to hold more water
              left += 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.max_area([5, 5, 3, 1, 4, 4, 3]))
    # Output: 20