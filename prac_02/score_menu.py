import random

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    get_choice()
    print("Thank you for use, see you.")


def get_choice():
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = random.randint(0, 100)
            print(f"Score is {score}")
        elif choice == 'P':
            get_result(score)
        elif choice == 'S':
            print('*' * score)
        else:
            print("Invalid input.")
        choice = input(">>> ").upper()


def get_result(score):
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    elif score <= 100:
        print("Excellent")


main()