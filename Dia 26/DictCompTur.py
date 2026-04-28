# Dictionary Comprehension
## Cria um novo dicionario a partir de uma lista
# new_dict = {new_key:new_value for item in list}

## Cria um novo dicionario a partir de um ja existente
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Tambem pode ser condicional
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}

# Funcao dict.item(Dicionario utilizado), passa por cada item do dicionario 1 por 1
passed_scores = {key:value for (key, value) in dict.items(students_scores) if value >= 60}

student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

# Data Frame = Aquela tabelinha
student_data_frame = pandas.DataFrame(student_dict)

# Loop through a data frame
# Panda tem um metodo especifico pra isso, bem mais eficiente
# Loop through rows of a data frame
# Passa por todas as linhas da data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    # Pode especificar cada informacao da linha. Ex:
    ## row.student -> Mostra so informacoes da chave student