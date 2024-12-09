integer = int(input("Enter an integer:"))
if integer%2 == 0:
    print("The given integer is divisible by 2")
elif integer%3 == 0:
    print("The given integer is divisible by 3")
elif integer%2 == 0 and integer%3 == 0:
    print("The given integer is divisible by both 2 and 3")
elif integer<=0:
    print("Integer must be a positive number")
else:
    print("The given integer is not divisible by 2 not by 3 and not by both")
