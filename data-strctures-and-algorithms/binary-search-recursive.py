def binary_search(list, low, high, value):
    if low > high:
        return None
    mid = low + ((high - low) // 2)

    if list[mid] == value:
        return str(value) + " is found"    
    elif value > list[mid]:
        return binary_search(list, mid + 1, high, value)
    else:
        return binary_search(list, low, mid - 1, value)

numbers = [1, 3, 5, 7, 8, 11]
print(binary_search(numbers, 0, len(numbers) - 1, 80))