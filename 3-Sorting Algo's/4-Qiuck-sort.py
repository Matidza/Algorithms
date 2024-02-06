def quicksort(arr,left,right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

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
quicksort(arr, 0, len(arr) -1)
print(arr)

# Practice
def quick(arr, left, right):
    """

    """
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
quicksort(arr, 0, len(arr) -1)
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

        #swapp the arr[i] and arr[j]
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] < pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

arr = [1,5,7,4,3,6,9,8,2,11,20,15,19,13,17,12,16,18,10,14]
quick(arr, 0, len(arr) -1 )
print(arr)