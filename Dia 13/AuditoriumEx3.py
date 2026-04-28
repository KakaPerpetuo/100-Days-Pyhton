target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:   # Ao inves de or tem que ser and, se nao toda vez q um numero for dividido por 3 e por 5 vai falar fizzbuzz
        print("FizzBuzz")
    elif number % 3 == 0:    # Trocar o if por elif
        print("Fizz")
    elif number % 5 == 0:    # Trocar o if por elif
        print("Buzz")
    else:
        print(number)   # Tirar o numero dos parenteses, nao queremos uma lista