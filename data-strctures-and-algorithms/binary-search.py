def binary_search(list, value):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == value:
            return str(value) + " is found"
        if value > list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None

numbers = [1, 3, 5, 7, 8, 11]
print(binary_search(numbers, 77))