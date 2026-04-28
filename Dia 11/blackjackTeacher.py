import os
import random
import art

def clear():
    """Funcao pra limpar o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Funcao para sortear uma carta aleatoria"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Funcao para calcular o total das cartas"""
    # Checagem de BlackJack no jogo inicial             # NOTA: Tem como checar se existe um elemento especifico em uma lista assim: if 11 in cards
    if sum(cards) == 21 and len(cards) == 2:    
        return 0
    
    # Checagem de Ace's no jogo inicial
    # Checar se um elemento esta na lista dessa forma é bem mais efetivo
    # Tentar usar sempre esse metodo
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """Funcao para decidir quem ganhou o jogo"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "Lose, you went over"
    elif computer_score > 21:
        return "Win, opponent went over"
    elif user_score > computer_score:
        return "Win"
    else:
        return "Lose"

def play_game():
    """Funcao principal do jogo"""

    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Tem como usar esse simbolo quando a variavel é indiferente
    # Soreteia as duas primeiras cartas do jogo
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Jogo contiua enquanto o jogador pedir cartas
    while not is_game_over:
    # Calcula o score de ambos
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # Se a funcao calculate_score retornar 0 ou 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: " )
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Jogada do computador
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Tambem usou funcao para iniciar o jogo
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
    