target = int(input())     # A number between 0 and 1000

sum = 0                                             

for number in range(0, target + 1, 2):        # Seleciona todos os numeros pares entre 0 e o numero pedido, inicia de
    sum += number                             # 0 pq pediu pares, Tem que somas + 1 para incluir tbm o numero pedido

print(sum)