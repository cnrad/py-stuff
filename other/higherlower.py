import random

def main():
    print("What would you like the range of guesses to be?")
    top = input("Your number: ")
    play(top)

def play(top):
    number = random.randint(1, int(top))

    print(f"Your Top Number: {top}")
    guessPrompt(number, top)

def guessPrompt(number, top):

    print("------------------------------")
    print(f"Guess a number between 1 and {top}")
    guess = input("Your guess: ")

    try:
        if int(guess) > int(top):
            print(f"Choose a number between 1 and {top}")
            return guessPrompt(number, top)

        if int(guess) < 0:
            print(f"Choose a number between 1 and {top}")
            return guessPrompt(number, top)

        if int(guess) == number:
            print(f"You got it, the number was {number}!")
            answer = input("\nPlay again? (y/n): ")
            if answer == "y":
                return main()
            else:
                return

        if int(guess) < number:
            print("Your guess was lower than the number! Choose again.\n")
            return guessPrompt(number, top)

        if int(guess) > number:
            print("Your guess was higher than the number! Choose again.\n")
            return guessPrompt(number, top)

        
    except ValueError:
        print("Please choose a number!")
        return guessPrompt(number, top)


main()