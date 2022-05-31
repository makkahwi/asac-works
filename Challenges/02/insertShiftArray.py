def insertShiftArray (arr, num) :
  if len(arr) % 2 == 0 :
    middle = len(arr) / 2 
  else :
    middle = int(len(arr) / 2) + 1

  newArr = []

  i = 0

  while (i < len(arr)) :
    if i == middle and newArr[len(newArr) - 1] != num:
      newArr.append(num)
    else :
     newArr.append(arr[i])
     i+=1

  return newArr