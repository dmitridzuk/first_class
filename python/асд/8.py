def coin_change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

amount = 100
coins = [1, 5, 10]
ways = coin_change(amount, coins)
print(f"Количество способов разменять сумму {amount}: {ways}")