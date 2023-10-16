def count_prizes(prizes: list) -> int:
    counter = 0
    for prize in prizes:
        if prize <= 3:
            counter += 1

    return counter


olympic_results = [int(x) for x in input().split()]
winner_num = count_prizes(olympic_results)
print(winner_num)

# возможно не понял условие