# Como abrir um arquivo - open("nome do arquivo")
# Salva o arquivo em uma variavel
file = open("my_file.txt")

# Como ler um arquivo - read()
# Funcao retorna o conteudo do arquivo
contents = file.read()
print(contents)

# Como fechar um arquivo - close("nome do arquivo")
# Precisa fechar pra nao prejudicar o funcionamento do computador
file.close("my_file.txt")

# Forma de fazer sem precisar fechar o arquivo
## Para escrever no arquivo tem que mudar o modo
## w - write - Apaga tudo que existia no arquivo
## r - read
## a - append -> Adiciona novas frases ao arquivo sem apagar o que estava anteriormente
## a+ - append and read
with open("my_file.txt", mode = "a+") as file:
    contents = file.read()
    print(contents)

    # Forma de escrever no arquivo - write("Frase que deseja adicionar no arquivo")
    # Deleta o que estava antes no arquivo
    file.write("\nNew text.")

# Se vc abrir um arquivo que nao existe ele sera criado
with open("new_file.txt", mode= "w") as file:
    file.write("New text.")


## PATHS
# Navegacao pelas pastas pra achar um arquivo
# Usa / para acessar os arquivos
# /Pasta1/Pasta2/Arquivo.txt
# ./ -> Olha na pasta atual
# ../ -> Retorna para a pasta anterior
# Usar isso pra acessar arquivos no codigo
# Absolute - Relative to the root
# Relative - Relative to the file youre in