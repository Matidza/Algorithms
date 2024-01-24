def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[0:len(arr)//2]
        right_arr = arr[len(arr)//2: len(arr)]

        #recursion
        merge_sort(left_arr) #sorted order
        merge_sort(right_arr)

        #merge 
        i = 0 # left_arr index
        j = 0 # right_arr index
        k = 0 #merged arr index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
arr = [ 1,5,7,9,4,6,3,8,2,5,4,7, 0,24,6,95,76,0,1,6,9,17,51]
merge_sort(arr)
print(arr)

def merge_sort(num):
    if len(num) > 1:
        left_num = num[0: len(num)//2]
        right_num = num[len(num)//2: len(num)]

        #reccursion
        merge_sort(left_num)
        merge_sort(right_num)

        #merge
        i = 0
        j = 0
        k = 0
        while i < len(left_num) and j < len(right_num):
            if left_num[i] < right_num[j]:
                num[k] = left_num[i]
                i += 1
            else:
                num[k] = right_num[j]
                j += 1
            k += 1

        while i < len(left_num):
            num[k] = left_num[i]
            i += 1
            k += 1
        while j < len(right_num):
            num[k] = len(right_num)
            j += 1
            k += 1
arr = [ -1,-5,-7,-9,-4,-6,3,-8,2,5,4,7, 0,-24,-6,-95,76,0,1,6,9,17,51]
merge_sort(arr)
print(arr)   
