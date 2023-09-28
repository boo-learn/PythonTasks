def luna_algo(card_num) -> bool:
    even_nums = [int(num) * 2 for num in str(card_num)[::2]]

    for index in range(len(even_nums)):
        if not even_nums[index] > 9:
            continue
        # 15 -> '15' -> ['1', '5'] - > [1, 5]
        # 283423876432874682746328764823764872368
        # 123 % 10 --> 3
        # 123 // 10 --> 12

        num_digits = list(str(even_nums[index]))

        even_nums[index] = sum(
            [int(x) for x in num_digits]
        )

    odd_nums = [int(num) for num in str(card_num)[1::2]]
    res_sum = sum(even_nums) + sum(odd_nums)
    return res_sum % 10 == 0
