import random


def main():
    display_menu()
    guess = int(input("\tGuess a number from 1 to 10: "))
    my_random = gen_random(1, 10)
    while guess != my_random:
        if guess < my_random:
            print("\tYour guess is smaller")
        elif guess > my_random:
            print("\tYour guess is bigger")
        guess = int(input("\tTry again: "))
    display_end(my_random)


def gen_random(_min, _max):
    my_random = random.randint(_min, _max)
    return my_random


def display_menu():
    print("*********Welcome to the Guessing Game*********")


def display_end(my_random):
    print("\tCorrect! it is ", my_random)
    print("Congratulations you win the game!")


if __name__ == "__main__":
    main()
