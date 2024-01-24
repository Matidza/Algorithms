def insertion_sort(arr):
    for i in range(1, len(arr)):
            j = i
            while arr[j -1] > arr[j] and j > 0: #swapping condition
                  arr[j-1], arr[j] = arr[j], arr[j-1] #Swapp
                  j -= 1

arr = [2, 6, 5, 1, 7, 9, 4, 8, 3,0]
insertion_sort(arr)
print(arr)

#arr = [2, 6, 5, 1, 7, 9, 4, 8, 3]
#print(sorted(arr))

#1
def insertion_sort(arr):
    """
    Sorting algo, sorting arr list
    """
    #The algorithm
    #An outer loop that goes from the 2nd element to the last element
    #(Throught the unsorted elemrnts)
    for i in range(1, len(arr)):
          j = i  
          while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -=1
      
arr = [1,5,7,4,3,6,9,8,2,11,20,15,19,13,17,12,16,18,10,14]
insertion_sort(arr)
print(arr)

#2
def insertion_sort(arr):
    """
    Sorting algo of arr list from largest to smallest
    """
    #The algorithm
    #An outer loop that goes from the 2nd element to the last element
    #(Throught the unsorted elemrnts)
    for i in range(1, len(arr)):
          j = i  
          while arr[j-1] < arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -=1
      
arr = [1,5,7,4,3,6,9,8,2,11,20,15,19,13,17,12,16,18,10,14]
insertion_sort(arr)
print(arr)