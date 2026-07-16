def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_part = merge_sort(arr[:middle])
    right_part = merge_sort(arr[middle:])

    sorted_list = []
    left_index = right_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            sorted_list.append(left_part[left_index])
            left_index += 1
        else:
            sorted_list.append(right_part[right_index])
            right_index += 1

    sorted_list.extend(left_part[left_index:])
    sorted_list.extend(right_part[right_index:])

    return sorted_list

values = [38, 27, 43, 3, 9, 82, 10]
result = merge_sort(values)

print("Sorted Array:", result)
