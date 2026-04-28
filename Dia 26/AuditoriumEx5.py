def convert(temp_c):
    """ Retorna a temperatura em F """
    temp_f = temp_c * (9/5) + 32
    return temp_f

# eval = tranforma o input diretamente em dicionario
weather_c = eval(input())

weather_f = {day:convert(weather) for (day,weather) in dict.items(weather_c)}

print(weather_f)