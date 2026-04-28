from art import logo, vs
from gameData import data
import random
import os

def clear():
    """ Funcao pra limpar o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """Use if statement to check if user is correct"""
    # Se a tem mais seguidores e a pessoa escolheu a, retorna True
    if a_follower > b_follower:
        return guess == "a"     # NOTA: Pode fazer dessa forma pra retornar True ou False, dependendo da resposta da sentenca
    # Mesma coisa so que ao contrario
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Making account at position B become the next at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

