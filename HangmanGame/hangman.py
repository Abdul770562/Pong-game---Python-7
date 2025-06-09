import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

#lives fo game over
lives=6
print(logo)
#randomly choosing a word
chosen_word = random.choice(word_list)
print(chosen_word)

#placeholder for _
placeholder=""
word_length=len(chosen_word)

#assigning placeholder according to length of word
for position in range(word_length):
    placeholder+="_"
print("word to guess=", placeholder)

game_over=False
#list used for repetative gueses
correct_letters=[]
#used for repetative gueses
while not game_over:
    print(f"----{lives}/6 lives-----")
    guess = input("Guess a letter to complete the word: ").lower()
    #used for printing of letters

    if guess in correct_letters:
        print(f"You've already guessed{guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"
    print(display)

    #for lives
    if guess not in chosen_word:
        lives-=1
        print(f"Wrong guessed letter {guess}")
        if lives==0:
            game_over = True
            print(f"it was {chosen_word}, You lose")



    if "_" not in display:
        game_over=True
        print("You win")

    #for diagram
    print(stages[lives])
