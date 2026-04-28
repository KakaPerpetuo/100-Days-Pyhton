# List Comprehension
## Cria uma nova lista de uma lista ja existente

# nova_lista = [item_adicionado for cada_item in lista_antiga]
# new_list   = [new_item        for item      in list]

numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

# Funciona pra Strings tbm, cria uma lista a partir da string
## Percorre em ordem
name = "Angela"
new_list = [letter for letter in name]
print(new_list)

# Tbm tem como usar a funcao range pra criar uma lista
range_list = [num*2 for num in range(1,5)]
print(range_list)

# Condicional List Comprehension
## Inclui uma condicional na criacao da lista
## Novo item so é adicionado se comprir com a condicional
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [item for item in names if len(item) < 5]

print(short_names)

upper_name = [item.upper() for item in names if len(item) > 5]
print(upper_name)