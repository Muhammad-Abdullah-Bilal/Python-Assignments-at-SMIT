num1 = int(input("Enter first number:"))
operator = input("Enter any one operator +,-,*,/:")
num2 = int(input("Enter second number:"))
if operator == '+':
   print(num1 + num2)
elif operator == '-':
   print(num1 - num2)
elif operator == '*':
   print(num1 * num2)
elif operator == '/':
   if num2!=0:
     print(num1 / num2)
   else:
      print("Error! Division by zero")
else:
    print("Invalid operator!")

