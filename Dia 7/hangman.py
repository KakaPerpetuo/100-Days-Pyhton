import random

# ToDo 1 - Step 5
import hangman_art
import hangman_words

# ToDo-1 - Step 1:
chosen_word = random.choice(hangman_words.word_list)
number_of_letters = len(chosen_word)

# ToDo-1 - Step 4:
lives = 6

# ToDo-3 - Step 5:
print(hangman_art.logo)
# Outra forma de fazer
# from hangman_art import logo, stages
# print(logo)

# Testing code - Step 2:
#print(f"Pssssst, the solution is {chosen_word}")

# ToDo-1 - Step 2:
display = ["-"] * number_of_letters

# Outra forma de fazer ToDo-1 - Step 2:
# display = []
# for letter in chosen_word:
#    display += "-"

# Outra forma de fazer Todo-1 - Step 3:
# end_of_game = False  <-

# ToDo-4 - Step 5
used_letter = []

# ToDo-1 - Step 3:
while "-" in display and lives > 0:
# while not end_of_game:  <-
    # ToDo-2 - Step 1:
    guess = input("Guess a letter: ")
    guess = guess.lower()

    # ToDo-4 - Step 5
    while guess in used_letter:
      print(f"You've already guessed {guess}")
      print(f"{' '.join(display)}")
      print(hangman_art.stages[lives])
      guess = input("Guess a letter: ")
      guess = guess.lower()
    # Outra forma de fazer - So checa se é a mesma letra que a pessoa acertou
    # if guess in display:
    #    print(f"You've already guessed {guess})

    # ToDO-3 - Step 1 * Modificacoes * ToDo-2 - Step 2:
    for n in range(number_of_letters):
        if chosen_word[n] == guess:
            display[n] = guess

    # Outra Forma de fazer:
    # for position in range(number_of_letters):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter

    # ToDo- 2 - Step 4:
    if guess not in display:
        # ToDo-5 - Step 5
        print(f"You guessed { guess}, that's not in the word. You lose a life") 
        lives -= 1

    # Outra forma de fazer:
    # if guess not in chosen_word:
    #    lives -= 1
    #    if lives == 0:
    #       end_of_game == True
    #       print("You Lose!")

    # ToDo-4 - Step 5
    used_letter.append(guess)
    # ToDo-3 - Step 2:
    print(f"{' '.join(display)}")
    # ToDo-3 - Step 4
    print(hangman_art.stages[lives])

if "-" not in display:
    print("You win!")
elif lives == 0:
    print("You lose!")
    print(f"The word was {chosen_word}")

# if "-" not in display:   <-
#    end_of_game = True  
#    print("You win!")

# print(stages[lives])