import functions

# Propt works until someone type off
## Flag pra parada do programa
is_working = True

while is_working:
    # 1. Prompt user by asking "What would you like? (espresso/latte/cappucino): "
    ## Pergunta o que o usuario quer
    coffee_choice = input("\tWhat would you like? (espresso/latte/cappuccino): ").lower()

    # Check the user's input to decide what to do next.
    # 2. Turn off the coffe machine by entering "off" to the prompt
    ## Interrompe o loop quando o usuario digita "off"
    if coffee_choice == "off":
        is_working = False

    # 3. Print report - show current resource value
    ## Printa os recursos quando pedido
    elif coffee_choice == "report":
        print(f"Water: {functions.resources['water']}ml")
        print(f"Milk: {functions.resources['milk']}ml")
        print(f"Coffee: {functions.resources['coffee']}g")
        print(f"Money: ${functions.resources['money']}")
    
    # EXTRA: Reabastecer suprimentos 
    ## Reabastece suprimentos quando pedido
    elif coffee_choice == "refuel":
        ### Pergunta ao usuario a quantidade que ele que q adicione
        resource = input("What do you want to refuel?: ").lower()
        ### Adiciona o produto desejado
        if resource == "water":
            functions.resources["water"] = functions.refuel_stock(functions.resources["water"], resource)
        elif resource == "milk":
            functions.resources["milk"] = functions.refuel_stock(functions.resources["milk"], resource)
        elif resource == "coffee":
            functions.resources["coffee"] = functions.refuel_stock(functions.resources["coffee"], resource)
        functions.clear_screen()
    
    # Chama a funcao de criar o cafe, so muda o nome de cada
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        functions.machine_working(coffee_choice, functions.resources)
    

            