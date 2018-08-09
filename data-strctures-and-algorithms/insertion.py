def insertion_sort(list):
    for i in range(1, len(list)):
        element = list[i]
        j = i - 1
        
        while list[j] > element and j >= 0:
            list[j + 1] = list[j]
            j -= 1

        list[j+1] = element

list = [5, 4, 3, 2, 1]
insertion_sort(list)
print(list)