def collatz_algo(num: int) -> list:
    stoppers = [4, 2, 1, 0]

    nums = []
    curr_num = 0

    while num not in stoppers:
        nums.append(int(num))
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1

    return nums
