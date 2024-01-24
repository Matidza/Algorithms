def merge_sort(arr):
    if len(arr) > 1:
        left = arr[0: len(arr)//2]
        right = arr[len(arr)//2: len(arr)]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [1, 5, 7, 9, 4, 6, 3, 8, 2, 5, 4, 7,
       0, 24, 6, 95, 76, 0, 1, 6, 9, 17, 51]
merge_sort(arr)
print(arr)
