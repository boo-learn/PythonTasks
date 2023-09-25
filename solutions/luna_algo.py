def luna_algo(card_num):
    num_string = str(card_num)
    even_nums = [int(num) * 2 for num in num_string[1::2]]

    for index in range(len(even_nums)):
        if even_nums[index] > 9:
            num_digits = list(
                str(
                    even_nums[index]
                )
            )
            even_nums[index] = sum(
                [int(x) for x in num_digits]
            )

    odd_nums = [int(num) for num in num_string[::2]]
    res_sum = sum(even_nums) + sum(odd_nums)
    if res_sum % 10 == 0:
        return 'Да'
    return 'Нет'

luna_algo(2223000048400011)