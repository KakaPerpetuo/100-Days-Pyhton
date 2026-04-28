# ToDo 1 - Step 4
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ToDo 1 - Step 1
def encrypt(text,shift):

    # ToDo 2 - Step 1
    result = ""
    for letter in text:                                                   ## Varre todas as letras do texto
        for n in range(len(alphabet)):                                    ## Percorre o alfabeto
            if letter == alphabet[n]:                                     ## Se a letra do texto for igual a do alfabeto
                result += alphabet[(n+shift) % len(alphabet)]             ## Resultado = Letra do alfabeto mais o numero pedido  % tamanho do alfabeto, caso a letra esteja no final

    return result

### Outra forma de fazer - Step 1
# def encrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letter in plain_text:
#       position = alphabet.index(letter)     NOTA: Forma de fazer com menos custo, usar a funcao index pra saber a posicao da letra pedida na lista
#       new_position = position + shift_amount
#       new_letter = alphabet[new_position]
#       cipher_text += new_letter
#    print(f"The encoded text is {cipher_text}")
# encrypt(text, shift)

# ToDo 1 - Step 2
def decrypt(text, shift):

    # ToDo 2 - Step 2
    result = ""
    for letter in text:
        position = alphabet.index(letter)                    
        new_position = position - shift
        # Nao precisa fazer isso pq python entende numero negativo como a lista de tras pra frente
        #if new_position < 0:                                  
            #new_position = len(alphabet) + new_position
        new_letter = alphabet[new_position]
        result += new_letter
    return result

### Outra forma de fazer - Step 2
# Ficou praticamente igual

# ToDo 1 - Step 3 - COMBINAR AS DUAS FUNCOES
def ceaser(text, shift, direction):
    result = ""
    for letter in text:
        # ToDo 3 - Step 4
        if letter not in alphabet:
            result += letter
        else:
            position = alphabet.index(letter)
            if direction == "encode":
                result += alphabet[(position + shift) % len(alphabet)]
            elif direction == "decode":
                result += alphabet[position - shift]
    
    print(f"The {direction} text is {result}")

### Outra forma de fazer - Step 3
# def cease(start_text, shift_amount, cipher_direction):
#    end_text = ""
#    if cipher_direction == "decode":
#       shift_amount *= -1            ->    Raciocinio legal: a unica diferenca entre os dois shifts é somar e diminuir
#    for letter in start_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#    print(f"The {cipher_direction} text is {end_text})

# ToDo 1 - Step 4
print(art.logo)

continue_ceaser = True

while continue_ceaser:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # ToDo 2 - Step 4
    if shift > len(alphabet):               # Se o numero escolhido for muito maior q o alfabeto = Faz um modulo pra ajustar
        shift = shift % len(alphabet)
    ### Outra forma de fazer - Step 4
    # shift = shift % 26                    # Se o numero for pequeno nao vai mudar entao n precisa do if

    # ToDo 2 - Step 3
    ceaser(text, shift, direction)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if answer == "no":
        continue_ceaser = False
        print("Goodbye!")