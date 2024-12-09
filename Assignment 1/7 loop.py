num = int(input("Enter any number:"))
i = 1
factorial = 1
while (i <= num):
  factorial *= i
  i += 1
print("The factorial of", num, "is:", factorial * i)
