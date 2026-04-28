# GUI - Graphical User Interface
# Pode importar assim: from tkinter import *, para importar todas as classes
import tkinter

# Equivalente a screen do turtle
# Inicializacao da Classe Tk()
window = tkinter.Tk()
# Muda o titulo da janela
window.title("My first GUI Program")
# Valor minimo e inicial da janela
window.minsize(width=500, height=300)

# Label
# Inicializa a clase Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# Definir como o componente vai aparecer na janela
## Funcao pack, coloca a Label no centro da janela
# Pode colocar em varias opcoes de lugares
# Usando side
# Tem como mudar muitas coisas
# Advanced Python Arguments
## Deixar claro qual parametro quer
# Place usa coordenadas
# Grid usa coluna e linha
my_label.place(x=0, y=0)
# Formas de mudar o texto
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

## Funcao para adicionar alguma utilidade ao botao
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
## Button class
# Command = da uma funcao ao botao
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

# Classe Entry para aparecer opcao de escrever na janela 
input = tkinter.Entry()
input.insert(0, string="Some text to begin with.")
input.pack()
# Metodo para retornar oq foi escrito na caixinha
answer = input.get()

# Text

# Classe que faz tipo uma caixinha de texto
text = tkinter.Text(height=5, width=30)
text.focus()
# Adiciona textos no inicio
# text.insert(0, "Exemple of multi-line text entry.")
# print(text.get("1.0", 0))
text.pack()

# Spinbox

# Caixinha pra selecionar numeros
def spinbox_used():
    # Pega o atual valor na spinbox
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Escala de valores
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Raiobutton
# Escolher diferentes opcoes
def radio_used():
    print(radio_state.get())
# Variavel para armazenar valor de qual opcao foi escolhida
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# ListBox
def listbox_used(event):
    # Armazena atual selecao da listbox
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Loop que mantem a janela aberta
## Tem que ficar no final do programa
window.mainloop()
