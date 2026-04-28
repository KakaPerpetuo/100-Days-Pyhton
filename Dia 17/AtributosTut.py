# Sintaxe:
# class name_of_class:

# Primeira letra da classe tem que ser maiuscula
class User:
    # Usa pra caso vc nao queira colocar nada na funcao ou classe
    pass

class User2:
    # Forma de inicializar valores no atributo
    # Inicializa sempre que um objeto dessa classe é criado
    def __init__(self,user_id, username):
        print("new user being created...")
        # Pode-se inicializar varios atributos aqui
        # Construtores
        self.id = user_id
        self.username = username
        # Pode inicializar um valor padrao para todos os objetos
        self.followers = 0

class Car:
    # Um construtor, coloca o valor q desaja acrescentar como parametro
    # Nao esquecer de colocar esse self
    # Melhor forma de fazer quando vai criar muitos objetos iguais
    def __init__(self, seats):
        self.seats = seats

# Assim que cria um objeto
user_1 = User()

# Formas de criar um atributo, sem declarar na classe - Nao é tao eficiente
user_1.id = "001"
user_1.username = "Joao"

#user_2 = User2()

# Construtores
user_3 = User2("001", "Angela")
print(user_3.username)

# Passa o atributo na criacao do objeto, dessa forma sabe-se o valor do atributo
my_car = Car(5)