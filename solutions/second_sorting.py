def paycheck_best_sum(prices: list) -> list:
    prices.sort(reverse=True)
    breaking_index = len(prices) - len(prices) // 2
    best_sum = sum(prices[:breaking_index])

    return best_sum
