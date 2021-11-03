"""
Author: Anant
Date: 3/11/21
Purpose: Practice of python..
"""

import random


def main_game(a, b, user_name):
    number = random.randint(a, b)
    print(f"Guess the number between {a} and {b}")
    chances = 0
    while True:
        chances += 1
        choice = int(input())
        if choice == number:
            print(
                f"Correct {user_name} took {chances} trials to guess the number.")
            return chances
        elif choice > number:
            print("Wrong, guess a smaller number again")
        elif choice < number:
            print("Wrong, guess a greater number again.")


if __name__ == '__main__':
    a = int(input("Enter the lower element of range which you want to give: "))
    b = int(input("Enter the upper element of range: "))
    user1 = input("Enter the name of first player: ")
    user2 = input("Enter the name of second player: ")
    print(f"\nNow first turn is of {user1}")
    user1_trials = main_game(a, b, user1)
    print(f"\nNow second turn is of {user2}")
    user2_trials = main_game(a, b, user2)

    if user1_trials < user2_trials:
        print(f"{user1} wins by {user1_trials -  user2_trials} trials.")
        print(f"Congratulation {user1}")

    elif user2_trials < user1_trials:
        print(f"{user2} wins by {user2_trials -  user1_trials} trials.")
        print(f"Congratulation {user1}")

    elif user1_trials == user2_trials:
        print(
            f"Match draw between {user1} and {user2}, but they both performed well..")
