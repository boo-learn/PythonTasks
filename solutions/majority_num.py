from collections import Counter


class Solution:
    def majorityElement(nums: list[int]) -> int:
        nums_count = Counter(nums)
        for num in nums_count:
            if nums_count[num] >= len(nums) / 2:
                return num
