import random
from random import randrange


def _generate_number(difficulty):
    secret_number = int(random.uniform(1, difficulty))
    return secret_number


def _get_guess_from_user(difficulty):
    number = int(input(f"You need to guess a number between 1 to {difficulty}: "))
    return number


def _compare_results(secret_number, number):
    # checking if the number the user chose equal to the random number
    if secret_number == number:
        return True
    else:
        return False


def play(difficulty):
    print("Guess game start....")
    print("Generating a Number....")
    secret_number = _generate_number(difficulty)
    print(" The number is ready. Now it is Your turn")
    number = _get_guess_from_user(difficulty)
    if _compare_results(secret_number, number):
        print("you won")
        return True
    else:
        print("you Lose")
        return False
