from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_working = True

# Declaracao de todos os objetos que vao ser usados
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_working:

    # Opcoes de drinks disponiveis
    options = menu.get_items()

    # Pede para o cliente escolher entre os itens disponiveis e armazena o resultado numa variavel
    coffee_option = input(f"\tWhat would you like? ({options}): ").lower()

    # Caso o cliente digite "off" o programa para de funcionar - Igual o outro
    if coffee_option == "off":
        is_working = False
    
    # Mostra a quantidade de recursos
    elif coffee_option == "report":
        # Usa os metodos ja existentes dos objetos criados
        coffee_maker.report()
        money_machine.report()

    else:
        # Cria um objeto - MenuItem - de acordo com a escolha do drink
        drink = menu.find_drink(coffee_option)

        # Usa esse objeto criado para chamar os metodos necessarios para o funcionamento da maquina
        if coffee_maker.is_resource_sufficient(drink):  # Tem como fazer direto com and
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)