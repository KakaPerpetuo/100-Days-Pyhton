#student_dict = {
#    "student": ["Angela", "James", "Lily"], 
#    "score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
#    pass
#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TO-DO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#TO-DO 2. Create a list of the phonetic code words from a word that the user inputs.
palavra = input("Enter a word: ").upper()

result = [nato_dict[letra] for letra in palavra]

print(result)


