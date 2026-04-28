line1 = ["O", "O", "O"]
line2 = ["O", "O", "O"]
line3 = ["O", "O", "O"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input()

#position_list = list(position)   # Tranforma a variavel position em uma lista

# NAO PRECISA TRANSFORMAR A VARIAVEL EM LISTA
# Da forma abaixo ja é possivel selecionar cada posicao da string

letters = position[0]    # Posicao -> A B C
numbers = position[1]    # Lista   -> 1 2 3 

letters = letters.lower()     # Coloca as letras em minusculo

#OUTRA FORMA DE FAZER TBM

#abc = ["a", "b", "c"]  -> Cria uma lista das possiveis letras
#letter_index = abc.index(letter)  -> Funcao que mostra em que posicao da lista pedida esta a variavel pedida ( )
#number_index = int(position[1]) - 1  -> Pega a posicao do numero digitado
#map[number_index][letter_index] = "X"  -> Adiciona X no local desejado no mapa

##########################################################################################################################

if letters == "a":            # Transforma as letras nos numeros relacionados
    letters = 1
elif letters == "b":
    letters = 2
else:
    letters = 3

map[int(numbers) - 1][int(letters) - 1] = "X"   # map[Lista][Posicao na lista], coloca x na posicao desejada

print(f"{line1}\n{line2}\n{line3}")

