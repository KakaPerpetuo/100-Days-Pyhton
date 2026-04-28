# Arguments with Default Values
## Colocar valores pre definidos nas funcoes
# Exemplo: def my_function(a=1, b=2, c=3)

# Unlimited Arguments
# *args: Many Positional Arguments
# args = arguments
# Aceita qualquer numero de argumentos
# Transforma os argumentos em uma tupla

# Soma todos os valores independente da quantidade
def add(*args):
    soma = 0
    for n in args:
        soma = soma + n

    print(soma)

add(1, 2, 3)
add(2, 2, 2, 2, 2)
add(500, 1)

# **kwargs: Many Keyworded Arguments
# Tranforma argumentos em um dicionario
# Assim mais facil acessar valores especificos
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs:
        print(key)
        print(value)

    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# Forma mais dinamica de criar uma classe
# Funcao .get de um dict:
## Pega a informacao do valor que esta na chave pedida entre ( )
## Beneficio: Se a chave pedida nao existir no dicionario, o programa funciona normalmente 
# Forma de criar uma classe com varios valores opcionais
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GTR")