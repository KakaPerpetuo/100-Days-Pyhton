{"Bug": "An error", "Function": "A piece of code"}   ## -> Sintaxe do Dicionario - {chave:o que ela significa}

programming_dictionary = {                   ## Bom costume identar assim
    "Bug": "An error", 
    "Function": "A piece of code"
}

programming_dictionary["Bug"]      ## Acesso de informacao pela chave

# Adicionando novos itens ao dicionario
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Criando dicionario vazio ou apagando um ja existente
programming_dictionary = {}

# Editar um item ao dicionario 
programming_dictionary["Bug"] = "A moth"

# Loop pelo dicionario 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

## PODE COLOCAR LISTAS E OUTROS DICIONARIOS COMO VALORES DE UM DICIONARIO

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionaty
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5,
    },
}

# Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

import os
def clear_screen():                      ## NOTA: Funcao pra limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')