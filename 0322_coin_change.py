from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        MAX = math.inf
        dp = [MAX] * (amount+1)
        dp[0] = 0
        
        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
                    
        return dp[amount] if dp[amount] != MAX else -1
        

coins = [1,2,5]
amount = 11
# Output: 3

print(Solution().coinChange(coins, amount))