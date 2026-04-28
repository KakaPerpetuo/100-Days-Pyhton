print("Hello"[2])   # Se colocar esse numero na frente da string, ele vai selecionar apenas a letra indicada pela posicao do numero

"123" # Se colocar numeros entre aspas, eles sao considerados strings

123_345_678  # Pode dividir numeros muito grandes assim, o computador nao ve mudanca, é um inteiro

123.34 # Usar float, nao double

type(123) # Diz qual o tipo da variavelSS

str() # Converte pra string
int() # Converte pra int
float() # Converte pra float

3 + 5 # Soma
7 - 4 # Divisao
3 * 2 # Multiply
10 / 2 # Divisao, resultado vai ser um float
10 // 3 # Divisao inteira, resultado vai ser um inteiro
10 % 3 # Resto da divisao
10 ** 3 # Exponenciacao

round(8/3) # Funcao pra arredondar numeros
round(8/3, 2) # Funcao pra arredondar numeros com duas casas decimais, o segundo numero define as casas decimais

score = 0
# f-string
print(f"your score is {score}")  # Converte automaticamente pra string, facilitando impressao

"{:.2f}".format()  # Arredonda para a quantidade desajada de decimais