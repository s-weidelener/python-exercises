import random

number = random.randint(1, 100)
name = input("What's your name?\n: ")
tries = 0
max_tries = 10

while True:
    user_input = input(
        f"Hello {name}, please enter a number between 1 - 100\n: "
    )

    if not user_input.isdigit():
        print("Please enter a valid number")
        continue

    number_player = int(user_input)
    tries += 1

    if tries == max_tries - 1:
        print("That's your last try!")
    elif tries == max_tries:
        print("You lost the game, too many tries")
        answer = input("Do you wanna play another round (yes/no)? ").lower()

        if answer in ("n", "no"):
            print("Thank you for playing the game")
            break
        else:
            number = random.randint(1, 100)
            tries = 0
            print("New round started!")
            continue

    if number_player > number:
        print("Your number is too high")
    elif number_player < number:
        print("Your number is too low")
    else:
        print(f"You won the game in {tries} tries!")
        answer = input("Do you wanna play another round (yes/no)? ").lower()

        if answer in ("n", "no"):
            print("Thank you for playing the game")
            break
        else:
            number = random.randint(1, 100)
            tries = 0
            print("Nice, let's start!")