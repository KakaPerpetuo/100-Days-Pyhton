student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

maximo = 0                                             # Inicializa uma variavel com 0

for n in range(0, len(student_scores)):                # Utiliza a variavel n pra varrer toda a lista
    if student_scores[n] > maximo:                     # Faz uma comparacao, se o score na posicao n for maior do que o, 
        maximo = student_scores[n]                     # ate entao, score maximo, esse score maximo é substituido pelo da posicao n

# maximo = max(student_scores)  ->   Funcao max mostra o maior elemento da lista

print(f"The highest score in the class is: {maximo}")