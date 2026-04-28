student_heights = input().split()                    # Pede os numeros e ja separa todos em uma lista automaticamente

for n in range(0, len(student_heights)):             # Varre a lista, da primeira posicao ate a posicao total, usando range, funciona tipo o for em c
    student_heights[n] = int(student_heights[n])     # Transforma todos os elementos da lista em inteiros, de posicao em posicao

height_sum = 0                                       
contador = 0

for height in student_heights:                       # Cria uma variavel 'height' para varrer a lista
    height_sum += height                             # Soma todas as alturas
    contador += 1                                    # Conta quantas alturas tem

# height_sum = sum(student_heights)    ->     Essa funcao soma todos os elementos de uma lista

avarege_height = height_sum / contador               # Faz a conta da media

print(f"total height = {height_sum}")
print(f"number of students = {contador}")
print(f"avarege height = {round(avarege_height)}")