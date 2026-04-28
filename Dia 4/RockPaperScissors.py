import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# game_images = [rock, paper, scissors]   -> Coloca as imagens do jogo em uma lista, tentar buscar a forma mais facil de fazer 
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_choice = int(input())

# if user_choice >= 3 or user_choice < 0:                      
    # print("You type a invalid number, you lose!")

# else:
   # Resto do codigo igual

    # print(game_images[player_choice])  -> Vai printar a imagem de acordo com o que foi escolhido atraves da lista

computer_choice = random.randint(0, 2)

    # print(game_images[computer_choice])  -> Vai printar a imagem de acordo com o que foi escolhido atraves da lista

    ################ Outra forma de fazer ########################################

    # if player_choice == 0 and computer_choice == 2:
        # print("You Win")
    # elif computer_choice == 0 and player_choice == 2:
        # print("You lose")
    # elif computer_choice > user_choice:          ->  Na maior parte dos casos isso é real, menos do descrito no primeiro if, tentar perceber melhor esse tipo de acontecimneto
        # print("You lose")
    # elif user_choice > computer_choice:
        # print("You win")
    # elif computer_choice == player_choice:
        # print("It's a draw")

###############################################################################

if player_choice == 0:
    
    print(rock)
    print("Computer choice: ")
    
    if computer_choice == 0:
        
        print(rock)
        print("It's a draw")

    elif computer_choice == 1:
        
        print(paper)
        print("You lose")

    else:

        print(scissors)
        print("You win")
    
elif player_choice == 1:

    print(paper)
    print("Computer choice: ")

    if computer_choice == 0:
        
        print(rock)
        print("You win")

    elif computer_choice == 1:
        
        print(paper)
        print("It's a draw")

    else:

        print(scissors)
        print("You lose")

elif player_choice == 2:

    print(scissors)
    print("Computer choice: ")

    if computer_choice == 0:
        
        print(rock)
        print("You lose")

    elif computer_choice == 1:
        
        print(paper)
        print("You Win")

    else:

        print(scissors)
        print("It's a draw")
else:
    print("ERROR, type another number")
