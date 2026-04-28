class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath(self):
        print("I'm breathing")

# Uma classe pode herdar metodos e atributos de outra
## Basta colocar a classe mae entra parenteses quando estiver implementando a classe filha
# Ex:
class Fish(Animal):
    def __init__(self):
        # Chamar a init da classe mae junto a super
        super().__init__()

    # Forma de modificar um metodo ja existente na superclasse
    def breath(self):
        super().breath()
        print("Under water")
    
    def swim(self):
        print("I'm swimming")

nemo = Fish()
nemo.swim()
# Tambem tem os atributos e metodos da superclasse
nemo.breath()