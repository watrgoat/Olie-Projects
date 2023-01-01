numList = [6, 4, 7, 1, 2] 


# O(n) runtime 
def listSearch(numList, searchNum):
  for num in numList:
    if num == searchNum:
      return True
  return False

# is 2 in the list? -> yes/True
print(listSearch(numList, 2))