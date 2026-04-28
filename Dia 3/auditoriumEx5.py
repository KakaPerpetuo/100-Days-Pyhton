print("The Love Calculator is calculating your score...")

name1 = input()
name2 = input()

combined_names = name1 + name2  # combina duas strigs
lover_names = combined_names.lower()  #funcao lower coloca todas as letras em minusculo

t = lover_names.count("t")    #funcao count, conta quantas vezes a letra pedida entre parenteses aparece
r = lover_names.count("r")    #pega a variavel que contem a palavra que vc quer usar e usa o .count(caracter que quer procurar) a funcao retorna o numero de vezes que esse caracter aparece
u = lover_names.count("u")
e = lover_names.count("e")

first_digit = t + r + u + e

l = lover_names.count("l")  
o = lover_names.count("o")
v = lover_names.count("v")
e = lover_names.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))   # conversao de variaveis pode ser feita assim

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
