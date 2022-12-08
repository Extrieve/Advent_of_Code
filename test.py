def binary_search(iterator, value):
    left, right = 0, len(iterator) - 1
    while left <= right:
        mid = (left + right) // 2
        if iterator[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1
    return left + 1


print(binary_search([4, 3, 5, 2, 6, 1, 7], 5))