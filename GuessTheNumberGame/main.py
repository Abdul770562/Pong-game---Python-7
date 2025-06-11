from random import randint
from art import logo
print(logo)

Easylevel=10
Hardlevel=5

def check_answer(u_guess, actual_ans, turns):
    if u_guess > actual_ans:
        print("Too high.")
        return turns - 1
    elif u_guess < actual_ans:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_ans}")


def choose_difficulty():
    level=input("Choose an mode 'easy' or 'hard': ")
    if(level== "easy"):
        return Easylevel
    if(level=="hard"):
        return Hardlevel


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The answer is {answer}")

    turns=choose_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was{answer}")
            return
        elif guess != answer:
            print("Guess again.")

main()
