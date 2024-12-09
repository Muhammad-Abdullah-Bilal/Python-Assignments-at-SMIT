side1 = int(input("Enter the first side of a triangle:"))
side2 = int(input("Enter the second side of a triangle:"))
side3 = int(input("Enter the third side of a triangle:"))
# First method
#if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
#    print("It is a valid triangle")
#else:
#    print("It is not a valid triangle")

# Second method
if side1+side2+side3 == 180:
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle")
