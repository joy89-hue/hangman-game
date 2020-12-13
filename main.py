import os
from random import choice
from hangman_art import stages
from hangman_words import word_list

chosen_word = choice(word_list)

print(f"The solution is {chosen_word}")
lives = 6
display = []
for _ in chosen_word:
    display.append("_")

game_finished = False
while not game_finished:
    guess = input("Guess a letter: ").lower()
    cls = lambda: os.system('cls')
    cls()

    if guess in display:
        print("You've already guessed the letter {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the chosen word. You lose a life!")
        lives -= 1
        if lives == 0:
            game_finished = True
            print("You lose!")
    print(" ".join(display))

    if "_" not in display:
        game_finished = True
        print("You win!")

    print(stages[lives])

    

            




