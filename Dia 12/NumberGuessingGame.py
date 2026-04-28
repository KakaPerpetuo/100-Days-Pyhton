import random
import art

def choose_random_number():
    """Random number generator"""
    return random.randint(1, 100)

def compare(guess, ramdom_number):
    """Compara o numero pedido com o sorteado"""
    if guess > ramdom_number:
        print("Too high.")
        print("Guess again.")
    elif guess < ramdom_number:
        print("Too low.")
        print("Guess again.")
    else:
        print(f"You got it! The answer was {ramdom_number}.")
        # Se o numero for achado, retorna true para acabar o jogo
        return True

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = choose_random_number()

#print(f"Pssst, the correct answer is {random_number}")

# Variavel para armazenar dificuldade escolhida
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : " ).lower()

# Unica coisa que muda entre os dois jogos é a quantidade de tentativas, aqui elas sao definidas
if difficulty == "easy":
    attempts = 10 
elif difficulty == "hard":
    attempts = 5

# O jogo continua enquanto ainda existem tentativas
while attempts > 0:
        
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        # Se a funcao compare retornar True é pq o numero foi achando, entao quebra o loop
        if compare(guess, random_number) == True:
            break
        
        attempts -= 1
        
        # Se o numero de tentativas acabar, quebra o loop e mostra a resposta correta
        if attempts == 0:
            print(f"You've run out of guesses, you lose. The correct answer was {random_number}.")
        