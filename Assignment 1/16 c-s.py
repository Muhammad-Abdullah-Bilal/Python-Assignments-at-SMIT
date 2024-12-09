side1 = int(input("Enter the length of first side of a triangle:"))
side2 = int(input("Enter the length of second side of a triangle:"))
side3 = int(input("Enter the length of third side of a triangle:"))
if side1 == side2 == side3:
    print("This is equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
elif side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Lengths of sides must be positive numbers.")
else:
    print("The triangle is scalene.")
