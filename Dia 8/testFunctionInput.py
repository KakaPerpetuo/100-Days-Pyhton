def greet(name):                     ## -> NOTA: Assim que se faz uma funcao com parametro em python
    print(f"Hello {name}")
greet("Kaka")

# Funcoes com mais de 1 parametros
def greet_with(name, location):
    print(f"Hello {name} from {location}")

greet_with("Kaka", "Op")
# Key word arguments
greet_with(location="Op", name="Kaka")   # Da pra especificar os argumentos assim tbm