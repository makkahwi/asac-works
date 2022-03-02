def fibonacci(n) :
  result = [0, 1]

  i = 2

  while (i < n) :
    result.append(result[i - 1] + result[i - 2])
    i+=1
  
  print(result)

num = input()

fibonacci(int(num))