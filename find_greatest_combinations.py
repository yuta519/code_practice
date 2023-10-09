# Reference: https://www.momoyama-usagi.com/entry/info-algo-dp#f-8227b105


def find_greatest_combinations(cards: list[int], limit: int) -> int:
    dp = [[0 for _ in range(limit + 1)] for _ in range(len(cards))]

    for i in range(len(cards)):
        for j in range(len(dp[i])):
            if cards[i] <= j:
                if cards[i] + dp[i - 1][j - cards[i]] > dp[i - 1][j]:
                    dp[i][j] = cards[i] + dp[i - 1][j - cards[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
    return max([d[limit] for d in dp])


print(find_greatest_combinations([4, 6, 8], 10))
print(find_greatest_combinations([4, 6, 8], 11))
print(find_greatest_combinations([4, 6, 8], 12))
print(find_greatest_combinations([4, 6, 8], 13))
print(find_greatest_combinations([4, 6, 8], 14))
print(find_greatest_combinations([4, 6, 8], 15))
print(find_greatest_combinations([4, 6, 8], 16))
print(find_greatest_combinations([4, 6, 8], 17))
print(find_greatest_combinations([4, 6, 8], 18))
print(find_greatest_combinations([4, 6, 8], 19))
print(find_greatest_combinations([4, 6, 8], 20))
