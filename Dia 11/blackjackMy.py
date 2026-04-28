import functionMy

continue_game = True

# Jogo pode ser jogado enquanto o jogador quiser
while continue_game:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if answer == 'y':
        user = []
        computer = []
        functionMy.game_begin(user, computer)
        if functionMy.game_begin != False:
            functionMy.game(user, computer)
    else:
        continue_game = False
        print("Thanks for playing!")