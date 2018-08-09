def bubblesort(list):
    for i in range(len(list) - 1, 0, -1):
        for index in range(i):
            if list[index] > list[index + 1]:
                list[index], list[index + 1] = list[index + 1], list[index]

list = [19,12,11,9, 8, 7,3]
bubblesort(list)
print(list)