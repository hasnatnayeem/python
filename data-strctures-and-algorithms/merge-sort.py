def mergesort(unordered_list):
    length = len(unordered_list)
    if (length <= 1):
        return unordered_list

    mid = length // 2
    left_list = unordered_list[:mid]
    right_list = unordered_list[mid:]

    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return merge(left_list, right_list)
    

def merge(left_list, right_list):
    res = []
    while len(left_list) !=0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0])

    if len(left_list) == 0:
        res += right_list
    else:
        res += left_list
    
    return res


list = [5, 4, 3, 2, 1]
print(mergesort(list))