numbers = [2, 4, 7, 8, -2, 0, 9]

nums_iterator = iter(numbers)

for first, second in zip(nums_iterator, nums_iterator):
    print(first, second)
