import pandas
# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Usa-se pandas.DataFrame() -> Criar uma nova DataFrame
data = pandas.DataFrame(data_dict)
# Converter pra um arquivo csv -> .to_csv("Nome do arquivo")
data.to_csv("new_data.csv")