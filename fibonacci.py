memo: dict[int, int] = {1: 1, 2: 1}


def fibonacci(i: int) -> int:
    if i not in memo:
        memo[i] = fibonacci(i - 1) + fibonacci(i - 2)
        print(memo)

    return memo[i]


print(fibonacci(10))
