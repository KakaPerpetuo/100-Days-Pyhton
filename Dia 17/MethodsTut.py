class Car:
    def __init__(self):
        self.seats = 5

    # Metodos: igual qualquer outra funcao
    def enter_race_mode(self):
        self.seats = 2

my_car = Car()
print(my_car.seats)

# Chamamos o metodo dessa forma
my_car.enter_race_mode()
print(my_car.seats)


