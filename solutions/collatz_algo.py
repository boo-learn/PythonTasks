def collatz_algo(num: int) -> list:
    stoppers = [4, 2, 1]

    nums = []

    while num not in stoppers:
        nums.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1

    return nums
