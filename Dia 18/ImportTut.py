# Basic Import:
# keyword - Module name
import turtle
# Precisa chamar a pasta assim para conseguir acessar a classe
tim = turtle.Turtle()

# from... import...
# Melhor pra nao ficar escrevendo pontos
# keyword - Module name - keyword - Thing in Module
from turtle import Turtle
# Nao precisa ecrever o nome do modulo/pasta
tim = Turtle()
tom = Turtle()
terry = Turtle()

# import everything:
# Dessa forma vc importa tudo que tem no metodo
from turtle import *
# Mais dificil de visualizar 
# Nao é uma boa pratica

# Aliasing Modules:
# Da um novo nome ao modulo, nome que vc quiser
# keyword = Module name - keyword - alias name
import turtle as t
# Bom pra usar em modulos grandes
tim = t.Turtle()

# Installing Modules
# Baixar modulos da internet, pesquisar e baixar
# Baixa pelo site python packeges
# Instalar pelo terminal
import heroes # -> precisa instalar

# Prestar atencao com a diferenca entre python 2 e 3
