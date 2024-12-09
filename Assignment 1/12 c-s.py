temperature = int(input("Enter temperature in celcius: "))
if temperature<=0:
    print("The temperatute is freezing")
elif temperature>0 and temperature<=25:
    print("The temperature is moderate")
else:
    print("The temperature is hot")
