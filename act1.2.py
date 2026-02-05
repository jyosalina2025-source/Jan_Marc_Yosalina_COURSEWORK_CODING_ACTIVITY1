Nunber = 4

while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess < Nunber:
        print("Too low!")
    elif guess > Nunber:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
        break