# Lista é uma estrutura de dados
# Para armazenar muitas informacoes juntas

# fruits = [item1, item2] -> isso é uma lista

states_of_america = ["Delawwre", "Pennsylvania"]  # Pode colocar quantos elemesntos quiser

# ordem dos elementos é importante

print(states_of_america[0])  # para acessar o primeiro elemento

print(states_of_america[1])  # para acessar o segundo elemento, e assim por diante

print(states_of_america[-1])  # para acessar o ultimo elemento, negativos conta de tras pra frente

# E possivel editar elementos da lista

states_of_america[1] = "Pencilvania"

print(states_of_america)

# E possivel adicionar mais elementos a lista

states_of_america.append("New York")  # Funcao append adiciona o elemento pedido entre ( ) ao final da lista

print(states_of_america)

# Existem muitas funcoes para usar com listas

print(len(states_of_america))  # Mostra quantos elementos tem na lista

states_of_america.extend(["Divinolandia", "Ouro Preto", "Virginopolis"])  # Adiciona varios elementos a lista, nao coloca a palavra completa, tem que criar uma lista dentro do parenteses

print(states_of_america)

states_of_america.insert(1, "New Jersey")  # Insere um elemento na posicao pedida, coloca a posicao desejada e o elemento ( )

print(states_of_america)

states_of_america.remove("New Jersey")  # Remove um elemento da lista

print(states_of_america)

states_of_america.pop(2)  # Remove elemento da posicao pedida
states_of_america.pop()  # Remove o ultimo elemento da lista

print(states_of_america)

#states_of_america.clear() -> Remove todos os elementos da lista

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Como separar essa lista em dois elementos? Ex: Frutas e Vegetais, Ou fazer uma lista de listas?

fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]  # Uma lista de listas 

print(dirty_dozen)  # Aparece printado duas listas separadas dentro de uma grande

print(dirty_dozen[0])  # Printa apenas a primeira lista do compilado de lista
print(dirty_dozen[1])  # Pode printar a lista que quiser a partir do numero

print(dirty_dozen[1][2])  # Printa o elemento na posicao 2 da lista na posicao 1
print(dirty_dozen[1][3])

