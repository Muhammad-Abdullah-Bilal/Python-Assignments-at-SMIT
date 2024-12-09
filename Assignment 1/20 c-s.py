num = int(input("Enter a number:"))
if num < 2:
    print("The given number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("The given number is not prime")
            break
    else:
        print("The given number is prime")
