fruits = ["Apple", "Peach", "Pear"]   # Uma lista comum

for fruit in fruits:   # Cria uma variavel que representa cada elemento da lista -> Depende de lista
    print(fruit)       # Varre a lista assim, facilmente
    print(fruit + " Pie")        

print(fruits)          # Identacao é importante

# range(a, b) -> retorna a quantidade de elementos entre a e b

for number in range(1, 10):   # Conta do 1 ate 10 - 1 
    print(number)

print("------------")

for number in range(1, 10, 2):   # Conta do 1 ate 10, pulando de 2 em 2
    print(number)

print("------------")

soma = 0
for number in range(1, 101): 
    soma += number
print(soma)