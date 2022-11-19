guesses = 9
used = 0
while True:
    print("Guess remaining:", guesses)
    print("Enter the number you guessed")
    guess = int(input("Hint: number is between 0-50. So your guess is: "))

    if guesses != 0:
        number = 30
        guesses = guesses - 1
        if guess == number:
            print("Right answer...")
            print("You finished in ", used, " guesses..")
            break
        elif guess > number:
            print("You guess high...")

            used += 1
        elif guess < number:
            print("You guess low...")

            used = used + 1
        continue
    elif guesses == 0:
        print("Out of guesses, Game Over....")
        break
