firstNum = int(input("Enter first number:"))
secondNum = int(input("Enter second number:"))
if firstNum>secondNum:
    print("The largest number is" + str(firstNum) + ".")
elif secondNum>firstNum:
    print("The largest number is " + str(secondNum) + ".")
else:
     print("Both numbers are equal .")

