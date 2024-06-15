def insertion_sort(arr):
    for i in range(1, len(arr)):
            j = i
            while arr[j -1] > arr[j] and j > 0: #swapping condition
                  arr[j-1], arr[j] = arr[j], arr[j-1] #Swapp
                  j -= 1

arr = [2, 6, 5, 1, 7, 9, 4, 8, 3,0]
insertion_sort(arr)
print(arr)


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



def quick(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick(arr, left, partition_pos -1)
        quick(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

arr = [ 22, 11, 88, 66, 55, 77, 33, 44]
quick(arr, 0, len(arr) -1)
print(arr)
