def sum_series(n,first = 0,second = 1,type = "Fibonacci") :
  result = [first, second]

  i = 2

  while (i < n) :
    result.append(result[i - 1] + result[i - 2])
    i+=1
  
  print(type, "item no", n, "is",result[len(result)-1])

def fibonacci(n) :
  sum_series(n)

def lucas(n) :
  sum_series(n,2,1,"Lucas")

num = input()

fibonacci(int(num))
lucas(int(num))