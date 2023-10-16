def price_sort(prices: list) -> list:
    window_size = 2
    curr_index = 0
    while curr_index + window_size <= len(prices):
        # O = n/2
        if prices[curr_index] < prices[curr_index + 1]:
            prices[curr_index], prices[curr_index + 1] = prices[curr_index + 1], prices[curr_index]
        curr_index += 2

    if len(prices) % 2 > 0 and len(prices) > 1:
        if prices[-2] > prices[-1]:
            prices[-2], prices[-1] = prices[-1], prices[-2]

    return prices

# prices = input().split()
# prices = [int(i) for i in prices]
# sorted_prices = price_sort(prices)
# max_paycheck = sum([sorted_prices[i] for i in range(len(sorted_prices)) if i % 2 == 0])
# print(max_paycheck)

