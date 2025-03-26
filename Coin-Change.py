class Solution(object):
    def coinChange(self, coins, amount):
        \\\
        :type coins: List[int]
        :type amount: int
        :rtype: int
        \\\
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
            
        return dp[amount] if dp[amount] != float('inf') else -1
        