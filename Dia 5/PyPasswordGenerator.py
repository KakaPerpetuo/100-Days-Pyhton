import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

################################################# Meu jeito #############################################################################################

# Easy 

password = ""

for n in range(0, nr_letters):
    password += random.choice(letters)     # NOTA: Funcao random.choice, escolhe um elemento aleatorio de uma lista e vai adicionando a string password

for n in range(0, nr_numbers):
    password += random.choice(numbers)

for n in range(0, nr_symbols):
    password += random.choice(symbols)

print(f"Easy: {password}")

# Hard

# Soma o total de caracteres da senha
numbers_of_carac = nr_letters + nr_numbers + nr_symbols   
# Lista "password", preenchida dessa forma por espacos vazios multiplicados pelo numero total de caracteres da senha         
password = [""] * numbers_of_carac    # NOTA: Cria uma lista vazia com numeros pre determinados de elementos dessa forma
# Cria uma lista vazia onde serao armazenadas as posicoes da senha que ja foram utilizadas
number_of_carac_list = []             # NOTA: Lista vazia normal

# Contadores para saber se todos os elementos pedidos na senha foram devidamente adicionados
count_letters = 0
count_numbers = 0
count_symbols = 0

# For para adicionar as letras aleatorias na senha
for n in range(0, nr_letters):
    # While para se certificar se a quantidade de letras pedida foi colocada na senha
    # Programa continua enquanto todas forem colocadas
    while count_letters < nr_letters:
        # Funcao auxiliar para designar uma posicao aleatoria onde sera colocada a letra
        aux = random.randint(0, numbers_of_carac-1)          # Adicionado - 1 para nao dar erro por causa do tamanho da lista
        # If para checar se a posicao designada aleatoriamente esta ocupada
        if aux in number_of_carac_list:
            # Se estiver sorteia outra posicao
            aux = random.randint(0, numbers_of_carac)
        else:
            # Se a posicao estiver liberada, uma letra aleatoria é colocada nela
            password[aux] += random.choice(letters)
            # Como a posicao ja foi utilizada, ela é adicionada a lista de posicoes ja usadas
            number_of_carac_list.append(aux)
            # Como uma letra foi adicionada, o contador de letras é somado
            count_letters += 1


# For para adicionar os numeros na senha
# Identico ao outro
for n in range(0, nr_numbers):
    while count_numbers < nr_numbers:
        aux = random.randint(0, numbers_of_carac-1)
        if aux in number_of_carac_list:
            aux = random.randint(0, numbers_of_carac)
        else:
            password[aux] += random.choice(numbers)
            number_of_carac_list.append(aux)
            count_numbers += 1

# For para adicionar os simbolos na senha
# Identico ao outro
for n in range(0, nr_symbols):
    while count_symbols < nr_symbols:
        aux = random.randint(0, numbers_of_carac-1)
        if aux in number_of_carac_list:
            aux = random.randint(0, numbers_of_carac)
        else:
            password[aux] += random.choice(symbols)
            number_of_carac_list.append(aux)
            count_symbols += 1

print(f"Hard: {''.join(password)}")                         # NOTA: Funcao ''.join   ->  Pode usar pra transformar uma lista em uma string

######################################################## Jeito da prof ###############################################################################

# Easy: Ficou praticamente igual a que eu fiz

# Hard
password_list = []

for n in range(0, nr_letters):
    password_list += random.choice(letters)     

for n in range(0, nr_numbers):
    password_list += random.choice(numbers)

for n in range(0, nr_symbols):
    password_list += random.choice(symbols)

# Existe uma funcao que faz com uma linha o que eu fiz em 1 milhao ;(
random.shuffle(password_list)                                  # NOTA: Funcao random.shuffle(list) coloca os elementos de uma lista em ordem aleatoria

print(f"Tutor way \nHard: {''.join(password_list)}")

