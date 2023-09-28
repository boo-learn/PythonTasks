from collections import Counter


def singleNumber(nums: list[int]) -> int:
    counted_nums = Counter(nums)
    for num in counted_nums:
        if counted_nums[num] == 1:
            return num
