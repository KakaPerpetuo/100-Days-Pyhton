# Tabelas pre existentes ja formatadas
from prettytable import PrettyTable

table = PrettyTable()
#print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Forma de mudar uma variavel em python
table.align = "l"

print(table)



