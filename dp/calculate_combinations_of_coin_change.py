def calculate_combinations_of_coin_change(coins: list[int], amount: int):
    dp = [[0 for _ in range(0, amount + 1)] for _ in coins]

    for i in range(0, len(dp)):
        for j in range(0, len(dp[i])):
            if j == 0:
                dp[i][j] = 1
                continue
            if j - coins[i] < 0:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp)
    print(dp[len(coins)-1][amount])

calculate_combinations_of_coin_change([2, 3, 5], 11)
