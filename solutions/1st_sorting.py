numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]


def bubble_sort_reversed(nums: list) -> list:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

    return nums


numbers = bubble_sort_reversed(numbers)
five_biggest_el_sum = sum(numbers[:5])
