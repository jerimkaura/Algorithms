def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while start <= end:
        midpoint = start + (end-start) // 2
        midpoint_val = list[midpoint]
        if midpoint_val == item:
            return midpoint
        elif item < midpoint_val:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None


print(binary_search([6, 9, 12, 13, 22, 33, 34, 45, 56,
                     70, 89, 90, 90, 90, 91, 123, 987], 987))
