def add(x, y):

  return x + y

def subtract(x, y):

  return x - y

def multiply(x, y):
  
  return x * y

def divide(x, y):

  if y == 0:
    return 
  else:
    return x / y

result = add(5, 3)
print(result)

result = subtract(10, 4)
print(result)

result = multiply(2, 6)
print(result)

result = divide(15, 3)
print(result)