# Existe um site chamado AskPython para tirar duvidas

# Para usar a funcao random, precisa-se importar a biblioteca random 

import random # import é o que se usa em python para importar bibliotecas
import my_module # pode importar modulos criados por vc mesmo da mesma forma, muito mais facil

random_integer = random.randint(1, 10)  # Existem inumeras funcoes em random que podem ser chamadas atraves de random. Essa em especifico, escolhe um numero inteiro entre 1 e 10

print(random_integer)

print(my_module.pi)  # para acessar o modulo só fazer isso, usar o ., tipo c++

random_float = random.random()  # Escolhe um numero aleatorio entre 0.0 e 1.0, nao incluindo o 1

print(random_float)

# Para criar um random float maior q 1 é preciso apenas multiplica-lo

random_float = random.random() * 5

print(random_float)



 