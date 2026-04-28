# Describe Problem - Corrigido
# Descrever o problema para ser mais facil acha-lo
def my_function():
  for i in range(1, 21):    # Dessa forma o i só chega ate o valor 19, teria que colocar 21 pra resolver o probleama
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug - Corrigido
# As vezes o erro acontece apenas em situacoes especificas, tente reproduzi-lo pra saber que situacao é o erro
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)    # Em algum momento vai sortear o numero 6, que é maior que a lista, por isso pode dar bug
print(dice_imgs[dice_num])

# Play Computer - Corrigido
# Olhar cada detalhe do codigo para achar o erro
year = int(input("What's your year of birth?"))
if year >= 1980 and year <= 1994:         # O ano 1994 nunca vai ser escolhido dessa forma, precisa colocar =
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors - Corrigido
# As vezes o proprio programa mostra onde esta o erro
# As vezes tbm aparece no terminal
age = int(input("How old are you?"))          # De inicio, nao foi pedido um inteiro
if age > 18:
    print(f"You can drive at age {age}.")  # Aqui o erro esta sublinhado de vermelho, tbm nao tinha o fprint

#Print is Your Friend
# Colocar print em locais do codigo para descobrir onde o erro acontece
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: "))
print(word_per_page)                           # Assim percebemos que o erro esta no == 
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
# Usar sites pra descobrir onde esta o bug - Eu uso ChatGpt\
# Existem debuggers que explicam passo a passo
# Deve ter expansao no vsCode pra isso
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)            # Esse append nao estava dentro do for, por isso imprimia so um
  print(b_list)

mutate([1,2,3,5,8,13])

# 7. Take a break 
# 8. Ask a friend 
# 9. Run often - Sempre testar o codigo
# 10. Use stackOverflow
