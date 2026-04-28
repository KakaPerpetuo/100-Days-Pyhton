import art
import functions

print(art.logo)

# Pontos comecam em 0
points = 0

# Enquanto a pessoa acertar vai continuar verdadeiro
chose_right = True

# Escolhe dois instagrans aleatoriamente
insta_a = functions.choose_random()
insta_b = functions.choose_random()
# Pra nao ter mesma responta
while insta_a == insta_b:
    insta_b = functions.choose_random()

while chose_right:

    # Mostra os instagrans escolhidos e suas informacoes
    print(f"Compare A: {insta_a['name']}, a {insta_a['description']}, from {insta_a['country']}.")
    print(art.vs)
    print(f"Against B: {insta_b['name']}, a {insta_b['description']}, from {insta_b['country']}.")

    # Pede pro jogador escolher qual é o mais seguido
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Usa a funcao compare para dizer qual insta é o mais seguido
    answer = functions.compare(insta_a, insta_b)

    # Verifica se o jogador acertou
    if choice == answer:
        functions.clear()
        print(art.logo)
        points += 1
        print(f"You're right! Current score: {points}.")
        # Para o jogo continuar sequencialmente
        insta_a = insta_b
        insta_b = functions.choose_random()
        # Pra nao ter mesma responta
        while insta_a == insta_b:
            insta_b = functions.choose_random()
    # Se nao tiver acertado acaba o loop
    else:
        functions.clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {points}")
        play_again = input("Want to play again? (y/n): ").lower()
        if play_again == "y":
            # Comeca o jogo novamente
            points = 0
            insta_a = functions.choose_random()
            insta_b = functions.choose_random()
            functions.clear()
            print(art.logo)
        else:
            print("Thanks for playing")
            chose_right = False