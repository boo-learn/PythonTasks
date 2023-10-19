points = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1, 10]

points.sort(reverse=True)

count = 0
places_switch = 0

for index, point in enumerate(points):
    count += 1
    if point != points[index + 1]:
        places_switch += 1
    if places_switch > 2:
        break

print(count)
