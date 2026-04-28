# Calculadora

print(f"Digite uma conta:")
num1 = int(input())
operador = input()
num2 = int(input())

# Condicionais 
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
else:
    resultado = num1 / num2

print(f"O resultado é {resultado}")