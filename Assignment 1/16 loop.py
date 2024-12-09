num = int(input("Enter any number:"))
digit_sum = 0
if num < 10:
    digit_sum = num 
else:
   for digit in str(num):
    digit_sum += int(digit)

print("Sum of the digits:", digit_sum)


# 2nd method
#num = int(input("Enter an integer: "))
#digit_sum = 0
#while num > 0:
#    digit_sum += num % 10  
#    num = num // 10 
#print("Sum of the digits:", digit_sum)
