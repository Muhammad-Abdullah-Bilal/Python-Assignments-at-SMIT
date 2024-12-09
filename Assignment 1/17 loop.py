correct_number = 37
while True:
    guess = int(input("Guess the number (between 1 and 100):"))
    
    if guess == correct_number:
        print("Congratulations! You've guessed the correct number.")
        break 
    
    print("Wrong guess. Try again!")