percentage = int(input("Enter yout percentage:"))
if percentage >= 90:
    print ("Conragulation, you secure A grade.")
elif percentage >= 75 and percentage < 90:
    print ("You secure B grade.")
elif percentage >= 60 and percentage < 75:
    print ("You secure C grade.")
elif percentage >= 40 and percentage < 60:
    print ("You secure D grade.")
else:
    print ("You ave failed. Try next time.")

