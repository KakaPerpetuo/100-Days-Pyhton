sentence = input()

# .split() pode transformar uma frase em uma lista
lista_palavras = sentence.split()
result = {palavra:len(palavra) for palavra in lista_palavras}

print(result)