def price_sort(prices: list) -> list:
    window_size = 2
    curr_index = 0
    while curr_index + window_size <= len(prices):
        # O = n/2
        if prices[curr_index] < prices[curr_index + 1]:
            prices[curr_index], prices[curr_index + 1] = prices[curr_index + 1], prices[curr_index]
        curr_index += 2

    if len(prices) % 2 and len(prices) > 1:
        if prices[-2] > prices[-1]:
            prices[-2], prices[-1] = prices[-1], prices[-2]

    return prices
