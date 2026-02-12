Number = 4

while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess < Number:
        print("Too low!")
    elif guess > Number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")

        break
