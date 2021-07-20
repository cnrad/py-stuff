def bubbleSort(arr): #define function with "arr" argument
    n = len(arr) # get length of array
  
    
    for i in range(n-1): # cycle through all array elements
        for j in range(0, n-i-1): # cycle through the array from 0 to n-i-1
            
            if arr[j] > arr[j + 1] : # swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
# test array
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i]), # i forget what its called but interpolate sorted array