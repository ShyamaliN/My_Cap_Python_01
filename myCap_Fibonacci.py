#Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
#now we are using while loop to put the condition i.e. until count is less than/ equal to  n it should keep summing 
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

  
