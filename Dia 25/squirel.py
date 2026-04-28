import pandas

data = pandas.read_csv("squirel.csv")

contagem = data["Primary Fur Color"].value_counts()

new_data = pandas.DataFrame(contagem)
new_data.to_csv("squirrel_count.csv")


# ------------------------------- Outra forma ----------------------------------------

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_tut.csv")