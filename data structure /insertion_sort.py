def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


array = [1, 2, 7, 4, 9, 0, 2, 5, 8, 3]
insertionSort(array)
print(array)
