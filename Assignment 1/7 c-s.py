firstNum = int(input("Enter first number:"))
secondNum = int(input("Enter second number:"))
thirdNum = int(input("Enter third number:"))


if firstNum>=secondNum and firstNum>=thirdNum:
    print("The largest number is" + str(firstNum) + ".")
elif secondNum>=firstNum and secondNum>=thirdNum:
    print("The largest number is " + str(secondNum) + ".")
elif thirdNum>=firstNum and thirdNum>=secondNum:
    print("The largest number is " + str(thirdNum) + ".")
else:
    print("All the three numbers are equal")