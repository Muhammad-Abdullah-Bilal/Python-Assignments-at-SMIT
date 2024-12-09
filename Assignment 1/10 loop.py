num = int(input("Enter any number:"))
count = 0
if num < 10 and num > -10:
    count = 1
else:
# Convert the number to a string of its absolute value to avoid counting the negative sign
    for digit in str(abs(num)):
     count += 1
print("Number of the digits:", count)


# 2nd method
# num = int(input("Enter an integer: "))
# count = 0
# # Convert number to absolute to ignore negative sign
# num = abs(num)
# if num == 0:
#     count = 1
# else:
#     while num != 0:
#         num = num // 10  # Remove the last digit of num
#         count += 1 
# print("Number of digits:", count)

