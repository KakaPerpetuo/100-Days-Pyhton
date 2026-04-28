#################### Scope ##########################

enemies = 1

# Como nao passa enemies por parametro, a variavel dentro da funcao tem um valor diferente
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# Variaveis que so podem ser acessadas em determinado lugar, por exemplo dentro da funcao
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) # Erro, nao pode ser acessada desse forma pois so é valida dentro da funcao

# Global Scope
# Pode ser acessada em qualquer lugar do codigo
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)  # Como é uma variavel global, pode ser acessada dentro da funcao

drink_potion()
print(player_health) 

# Uma variavel ou funcao, so pode ser acessada dentro de onde ela foi criada, ou em funcoes que existem dentro de onde ela foi criada

# There is no Block Scope
game_level = 3
enemies = ["Skeletons", "Zombies", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# if, while, for... Nao contam pra bloquear, se criar uma variavel dentro de um deles, ela pode facilmente ser usada fora tbm

# Modifying Global Scope 
enemies = "Skeleton"
# Nao é uma boa ideia dar mesmo nome para variavel global e local, como acontece aqui
def increase_enemies():
    # Variavel nao esta sendo mudada, esta sendo criada uma nova variavel local
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Como modificar uma variavel global dentro de uma funcao?
enemies = 1
# Melhor evitar modificar variaveis globais, melhor usar return nas funcoes
def increase_enemies():
    # Para modificar uma variavel global dentro de uma funcao, usa-se a palavra reservada "global"
    global enemies 
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Tem que tomar cuidado ao usar variaveis globais, melhor evitar
# Podem ser uteis:
# GLOBAL CONSTANTS
# Variaveis que vc declara um valor uma vez e nunca mais muda

PI = 3.14
# Pode ser usada em todo o file, nao modificar
# Declarar com letra maiuscula, ai c sabe que é uma constante, ai vc vai saber que nao é pra modificar