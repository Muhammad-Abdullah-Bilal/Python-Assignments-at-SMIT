year = int(input("Enter any year:"))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("This is leap year")
else:
 print("This is not a leap year")