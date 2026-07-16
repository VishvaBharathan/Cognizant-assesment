def binary_search(values, key):
    start = 0
    end = len(values) - 1

    while start <= end:
        middle = (start + end) // 2

        if values[middle] == key:
            return middle
        elif key > values[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return None

data = [10, 20, 30, 40, 50, 60]
search_value = 40

position = binary_search(data, search_value)

if position is not None:
    print(f"Element found at position {position}")
else:
    print("Element not found")
