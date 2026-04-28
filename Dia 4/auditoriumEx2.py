import random   # importando a biblioteca random

names_string = input()  # Pedindo os nomes no terminal

names = names_string.split(", ")   # Separa os nomes de acordo com o que a é pedido em ( ) e coloca eles em uma lista

#random_name = random.choice(names) -> uma opcao de resolver mas nao é pra usae

number_of_names = len(names)  # Retorna quantos elementos tem na lista
random_number = random.randint(0, number_of_names - 1) # Escolhe um numero entre 0 e o numero maximo de elementos na lista, diminui de 1 pq comeca em 0

print(f"{names[random_number]} is going to buy the meal today!")