def binary_search(array, value):
    right = len(array)
    left = 0
    mid = len(array) // 2
    while left < right:
        if array[mid] == value:
            return mid
        elif value < array[mid]:

            right = mid
            mid = (left + right) // 2
        elif value > array[mid] and right - left > 1:
            left = mid
            mid = (left + right) // 2
        else:
            return None


arr = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(arr)+9):
    print(binary_search(arr, i))
