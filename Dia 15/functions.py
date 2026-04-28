import os

def clear_screen():                      ## Funcao pra limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu de tipos de cafes e ingredientes
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "money": 0,
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 5. Process coins
## Armazena a quantidade de cada moeda pedida pelo usuario e retorna uma lista com todas as moedas
def take_coins():
    """Function to take coins from the user and return a list of coins."""
    ### Cria uma lista vazia
    coins_list = []
    ### Pede ao usuario quantos quarters, dimes, nickles e pennies ele quer, essas quantias sao colocadas na lista em ordem
    print("Please insert coins: ")
    coins_list.append(int(input("how many quarters?: ")))
    coins_list.append(int(input("how many dimes?: ")))
    coins_list.append(int(input("how many nickles?: ")))
    coins_list.append(int(input("how many pennies?: ")))

    ### Retorna a lista com as quantidades de cada moeda
    return coins_list

# 4. Check resources sufficient?
## Checa se a quantidade de ingredientes disponiveis é suficiente pra fazer o cafe pedido
def check_resources(coffee_choice, resources):
    """ Check if it has enough resources to make the chosen coffee"""
    ### Compara os ingredientes necessarios para produzir o cafe com os ingredientes que tem na maquina
    if MENU[coffee_choice]["ingredients"]["water"] < resources["water"]:   # NOTA: Forma eficiente de se usar um dicionario
        if MENU[coffee_choice]["ingredients"]["coffee"] < resources["coffee"]:
            ### Como o espresso nao utiliza leite, no seu caso nao precisa fazer essa comparacao
            ### Retorna True se os ingredientes estiverem disponiveis
            if coffee_choice == "espresso":
                return True
            elif MENU[coffee_choice]["ingredients"]["milk"] < resources["milk"]:
                return True
    ### Retorna False se os ingredientes nao estiverem disponiveis, e especifica qual nao esta disponivel
            else:
                print("Sorry there is not enough milk. ")
                return False
        else:
            print("Sorry there is not enough coffee. ")
            return False
    else:
        print("Sorry there is not enough water. ")
        return False

# EXTRA: Funcao para reabastecer os ingredientes
def refuel_stock(value, name):
    ## Retorna o novo valor adicionado a quantidade reposta
    """Function to refuel the machine"""
    return value + int(input(f"How much {name} do you want to refuel?: "))

# 5. Process coins
## Faz a conta do valor que o usuario pagou
def coins_count(coins_list):
    """ Count the value that the user has given"""
    ### Retorna o valor pago, conta feita pela lista e valores de cada moeda
    return coins_list[0]*0.25 + coins_list[1]*0.1 + coins_list[2]*0.05 + coins_list[3]*0.01

# 6. Check transaction successful?
## Checa se o usuario pagou dinheiro suficiente
def transition_successful(paid_value, coffee_choice):
    """Check if the transaction was successful"""
    ### Compara valor pago com o valor do produto, retorna True se o valor for suficiente e False caso contrario
    if paid_value >= MENU[coffee_choice]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False
    
# 7. Make Coffee
## Funcao que atualiza os ingredientes depois que o cafe é feito
def make_coffee(coffee_choice, resources):
    """Function to take the ingredients needed from the resources and add the money"""
    resources["money"] += MENU[coffee_choice]["cost"]
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    ### Como espresso nao utiliza leite, pula o processo
    if coffee_choice != "espresso":
        resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    ### Oferece o produto para o usuario
    print(f"Here if your {coffee_choice}. Enjoy!")

# Funcionamento da maquina, usa as funcoes ja criadas
def machine_working(coffee_choice, resources):
    ## Se os ingredientes estao disponiveis
    if check_resources(coffee_choice, resources):
            ## Coloca as moedas adicionados em uma lista
            coins_list = take_coins()
            ## Conta o valor pago
            paid_value = coins_count(coins_list)
            ## Se o valor pago for o suficiente
            if transition_successful(paid_value, coffee_choice):
                ## Olha se precisa de troco
                if paid_value > MENU[coffee_choice]["cost"]:
                    change = paid_value - MENU[coffee_choice]["cost"]
                    print(f"Here is ${round(change, 2)} dollars in change.")
                ## Atualiza os ingredientes
                make_coffee(coffee_choice, resources)
