import random
import art
import os

# Lista do valor de cada carta, pra sortear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
def clear_screen():          
    """Funcao pra limpar o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def random_card(game_list):
    """Funcao para sortear uma carta aleatoria"""
    game_list.append(random.choice(cards))   

def game_print(user, computer):
    """Funcao para printar as cartas do jogador e do computador"""
    print(f"\tYour cards: {user}, current score: {sum(user)}")
    print(f"\tComputer's first card: {computer[0]}")

def print_final(user, computer):
    """Funcao para printar o placar final do jogador e do computador"""
    print(f"Game finished!!")
    print(f"Your final hand: {user}, final score: {sum(user)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")

def game_begin(user, computer):
    """Funcao para iniciar o jogo"""
    clear_screen()
    print(art.logo)

    # Coloca 2 cartas aleatorias em cada baralho
    for n in range(2):
        random_card(user)
        random_card(computer)
    
    game_print(user, computer)

    # Check se ocorreu BlackJack do usuario ou do Computador, no inicio do jogo
    if sum(user) == 21:
        print("Blackjack, User Wins")
        return True
    if sum(computer) == 21:
        print("Computer has a Blackjack, You lose")
        return True
    
def ace_check(user, computer):
    """Funcao para checar se o jogador tem um 'Ace'"""
    # Se o jogador tiver um 'Ace', ele pode ter um valor de 1 ou 11
    # Se o valor total do jogador ultrapassar 21, o valor do 'Ace' pode ser trocado para 1
    # Se depois que o valor for trocado, o total for menor q 21, o jogo continua
    if sum(user) > 21:
        for n in range(len(user)):
            if user[n] == 11:
                print("You have an 'Ace'!")
                user[n] = 1
                game_print(user, computer)

def game(user, computer):
    """Funcao para o jogo"""

    # Checagem de Ace's
    ace_check(user, computer)
    
    # Se o valor total do jogador ultrapassar 21 ele perde
    if sum(user) > 21:
        print_final(user, computer)
        print("You Lose :(!!")
        return 
    # Enquanto o valor nao ultrapassar 21 e a pessoa continuar pedindo cartas, o jogo continua
    else:
        got_card = True

        while got_card:
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == 'y':
                random_card(user)
                game_print(user, computer)
                game(user, computer)
                got_card = False
            # Jogador nao quer mais cartas, hora da jogada do computador
            else:

                # Enquanto o valor do computador for menor que 17, ele sorteia uma carta aleatoria
                while sum(computer) < 17:
                    random_card(computer)
                
                # Se o valor do computador ultrapassar 21, ele perde
                if sum(computer) > 21:
                    print_final(user, computer)
                    print("Opponent went over. You win :)!")
                    got_card = False
                    return
                # Se nao ultrapassar, o valor é comparado com o do jogador, decidindo assim quem ganha
                else:
                    if sum(user) > sum(computer):
                        print_final(user, computer)
                        print("You win :)!")
                        got_card = False
                        return
                    elif sum(user) < sum(computer):
                        print_final(user, computer)
                        print("You lose :(!)")
                        got_card = False
                        return
                    else:
                        print_final(user, computer)
                        print("It's a draw")
                        got_card = False
                        return