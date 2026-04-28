import art
import os

def clear_screen():                      ## Funcao pra limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_info(dictionary, name, value):
    dictionary[name] = value

def find_the_highest(dictionary):
    highest = 0
    for bidder in dictionary:
        if dictionary[bidder] > highest:
            highest = dictionary[bidder]
            highest_bidder = bidder
    return highest_bidder

## Funcao sem retorno
# def find_highest_bidder(bidding_record):
#    highest_bid = 0
#    winner = ""
#    for bidder in bidding_record:
#       bid_amount > highest_bid
#       highest_bid = bid_amount
#       winner = bidder
#    print(f"The winner is {winner} with a bid of ${highest_bid})

print(art.logo)
print("Welcome to the secret auction program")

audiction_dictionary = {}
bid_is_happening = True

while bid_is_happening:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    insert_info(audiction_dictionary, name, bid)
    # Outra forma de fazer - sem funcao
    # audiction_dictionary[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if answer == 'yes':
        clear_screen()
    else:
        bid_is_happening = False
        # Pode chamar a funcao aqui tbm
        # find_highest_bidder(audiction_dictionary)

highest_bidder = find_the_highest(audiction_dictionary)

print(f"The winner is {highest_bidder} with a bid of ${audiction_dictionary[highest_bidder]}")