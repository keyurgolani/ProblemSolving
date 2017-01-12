import random

def play_game():
    ready = raw_input("Think of a number between 1 and 10. Press any key when ready")
    guess_lower_bound = 1
    guess_upper_bound = 10
    for i in range(0, 5):
        guessed_number = random.randint(guess_lower_bound, guess_upper_bound)
        result = str(raw_input("Is the number you thought {}? y/N - ".format(guessed_number)))
        if result.lower() == "y":
            print("Great!")
            break
        else:
            hint = None
            while True:
                try:
                    hint = str(raw_input("Is {} LOWER or HIGHER? - ".format(guessed_number)))
                except NameError:
                    print("Please enter HIGHER or LOWER")
                except SyntaxError:
                    print("Please enter HIGHER or LOWER")
                except ValueError:
                    print("Please enter HIGHER or LOWER")
                else:
                    if(hint == "HIGHER" or hint == "LOWER"):
                        break
                    else:
                        print("Please enter HIGHER or LOWER")
            if(hint == "HIGHER"):
                guess_upper_bound = guessed_number - 1
            else:
                guess_lower_bound = guessed_number + 1
    else:
        print("Aww! I couldn't guess it. Give me one more chance.")

def main():
    while True:
        play_game()
        again = str(raw_input("Wanna play again? Y/n - "))
        if again.lower() == "n":
            break


main()
