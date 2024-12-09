num = int(input("Enter a number:"))
# Convert to string and reverse it
reversed_num = str(abs(num))[::-1]
# Add negative sign back if the original number was negative
if num < 0:
    reversed_num = "-" + reversed_num
print("Reversed number:", reversed_num)
