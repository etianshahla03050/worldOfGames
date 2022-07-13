import random


def _generate_sequence(difficulty):
    random_numbers = []
    for i in range(difficulty):
        random_numbers.append(int(random.uniform(1, 101)))
    print(random_numbers)
    return random_numbers


def _get_list_from_user(difficulty):
    # The user choose 5 numbers
    user_numbers = []
    print(f"Please Insert {difficulty} numbers")
    for i in range(difficulty):
        i = user_numbers.append(int(input("Enter  a Number: ")))
    return user_numbers


def _is_list_equal(random_numbers, user_numbers):
    # Checking if the lists are equal
    random_numbers.sort()
    user_numbers.sort()
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    print("Memory  game start....")

    random_numbers = _generate_sequence(difficulty)
    user_numbers = _get_list_from_user(difficulty)
    if _is_list_equal(random_numbers, user_numbers):
        print("you won")
    else:
        print("you Lose")
