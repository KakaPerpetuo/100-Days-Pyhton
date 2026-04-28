## Forma muito nao pratica
#with open("./weather_data.csv") as document:
#    weather_list_n = document.readlines()

## Metodo pra tirar \n da lista
#weather_list = [weather.rstrip('\n') for weather in weather_list_n]

# Biblioteca para ajudar no csv
# import csv

# with open("weather_data.csv") as data_file: 
    ## Le de forma mais pratica o conteudo de um arquivo csv, separa em fileiras
    # data = csv.reader(data_file)
    # tempetures = []
    # for row in data:
    #    if row[1] != "temp":
    #        tempetures.append(int(row[1]))

# print(tempetures)

# Biblioteca Pandas -> Ajuda na analise de dados
## Melhor forma de mexer com csv
import pandas

# read_csv = funcao da biblio panda usada para ler o arquivo
# Diferentemente dos outros metodos, os elementos vem formatados
data = pandas.read_csv("weather_data.csv")
# Para pegar os atributos de uma determinada coluna so precisa escrever o nome da coluna
data["temp"]

# DataFrame -> A tabela completa
# Series -> Uma unica coluna da tabela

# to_dict() -> Tranforma os dados em dicionario
data_dict = data.to_dict()

# to_list() -> Transforma a serie(Coluna) em uma lista
temp_list = data["temp"].to_list()

# Forma normal de fazer conta da media
average_temp = sum(temp_list) / len(temp_list)

# Forma de fazer conta da media usando Panda
## mean() -> Calcula media dos valores de uma serie
data["temp"].mean()

# max() -> Retorna o maior numero de uma Serie
data["temp"].max()

# Get Data in Columns -> Paga todas as informacoes de uma determinada coluna
data["condition"]
data.condition

# Get Data in Row -> Pega todas as informacoes de uma coluna
data[data.day == "Monday"]

# Forma de achar a coluna com o dia de maior temperatura
data[data.temp == data["temp"].max()]

# Forma de armazenar informacoes mais especificas de cada linha de um serie
monday = data[data.day == "Monday"]
monday.condition

# Forma de pegar o valor cru, sem informacoes
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Usa-se pandas.DataFrame() -> Criar uma nova DataFrame
data = pandas.DataFrame(data_dict)
# Converter pra um arquivo csv -> .to_csv("Nome do arquivo")
data.to_csv("new_data.csv")

