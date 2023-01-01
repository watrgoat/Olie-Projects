testList = [9, 2, 4, 6, 5, 5] 

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i-1
    key = arr[i]
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
  
  return arr


print(insertion_sort(testList))