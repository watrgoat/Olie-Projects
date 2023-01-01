beginList = [2, 5, 8, 3, 7]

# Time Complexity - O(n^2)
# Space Complexity - O(n)
def selectionSort(nums):
  out = []
  
  while nums:
    mini = min(nums)
    nums.remove(mini)
    out.append(mini)
  
  return out
  
print(selectionSort(beginList))