def threeSum(nums: list[int]) -> list[list[int]]:
    sums = []

    for index, num in enumerate(nums):
        for second_num in nums[index+1:]:
            for third_num in nums[index+2:]:
                if num + third_num + second_num == 0:
                    three_nums = [num, second_num, third_num]
                    three_nums.sort()
                    if three_nums not in sums:
                        sums.append(three_nums)

    return sums


print(threeSum([1, 2, -2, -1]))
