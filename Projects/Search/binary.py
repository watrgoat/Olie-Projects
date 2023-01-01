def binaryIterative(lst, srch):
  while True:
    n = len(lst)
    if lst[n//2] == srch:
      return True
    
    if n == 1:
      return False
    
    if srch < lst[n//2]:
      lst = lst[:n//2] # 1st half exluding the middle
    else:
      lst = lst[(n//2)+1:] # 2nd half including the middle 


def binaryRecursive(lst, srch):
  n = len(lst)
  if lst[n//2] == srch:
    return True
  if n == 1:
    return False
  
  if srch < lst[n//2]:
    return binaryRecursive(lst[:n//2], srch)
  else:
    return binaryRecursive(lst[(n//2):], srch)