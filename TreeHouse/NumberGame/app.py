import random

def play_game():
    # Generate Random Number between 1 and 10
    game_number = random.randint(1, 10)
    hit = False

    for i in range(0,5):
        # Ask User to Guess the Number
        guess = None
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
            except NameError:
                print("Please enter a number between 1 and 10")
            except SyntaxError:
                print("Please enter a number between 1 and 10")
            except ValueError:
                print("Please enter a number between 1 and 10")
            else:
                if guess < 1 or guess > 10:
                    print("Please enter a number between 1 and 10")
                else:
                    break
        # Tell them if it is exact match, too high or too low
        if guess == game_number:
            hit = True
            break
        elif guess > game_number:
            print("The guessed number is too high.")
        elif guess < game_number:
            print("The guessed number is too low.")

    # Declare the result.
    if hit:
        print("\n\n============= YOU GUESSED IT RIGHT ================")
    else:
        print("\n\n====== Please Try Again ======")


def main():
    while True:
        play_game()
        play_again = str(raw_input("Want to play again?\nEnter EXIT to exit the game."))
        if play_again == "EXIT":
            break


main()
