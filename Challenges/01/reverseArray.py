def reverseArray (arr):
  revArr = []

  i = len(arr) -1

  while i >= 0 :
    revArr.append(arr[i])
    i-=1
  
  return revArr